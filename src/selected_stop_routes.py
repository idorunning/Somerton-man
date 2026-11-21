#!/usr/bin/env python3
"""Selected-stop rail route test for the Somerton Man letters.

Implements docs/method/selected-stop-route-test.md exactly. Standard library only.

Each letter is read as a station where the traveller stopped. Between stops he
rides the shortest path on the 1938 metropolitan network. For each line the
cheapest assignment of stations to letters is found by dynamic programming and
compared with the same optimiser run on shuffled letters.

    python3 src/selected_stop_routes.py                 # full run, writes JSON
    python3 src/selected_stop_routes.py --draws 500     # quick run
"""
from __future__ import annotations

import argparse
import heapq
import itertools
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NETWORK = ROOT / "data/reference/sar-metro-1938-network.json"
OUTPUT = ROOT / "data/processed/selected-stop-routes-2026-11-21.json"

SKIP_PENALTY = 12
SEED = 19481130
HUB = "North Terrace"
LINES = {"L1": "WRGOABABD", "L3": "WTBIMPANETP", "L4": "MLIABOAIAQC", "L5": "ITTMTSAMSTGAB"}
CANCELLED = ("L2", "MLIAOI")
VARIANT_AXES = [("L1", 0, "WM"), ("L3", 0, "WM"), ("L4", -1, "CS"), ("L5", -3, "GC")]


# ---------------------------------------------------------------- network
def load_network(path=NETWORK):
    data = json.loads(path.read_text())
    adj, line_of = {}, {}
    for line in data["lines"]:
        st = line["stations"]
        for i, s in enumerate(st):
            line_of.setdefault(s, []).append((line["id"], i))
            adj.setdefault(s, {})
        for a, b in zip(st, st[1:]):
            adj[a][b] = adj[b][a] = 1
    for e in data["extra_edges"]:
        adj.setdefault(e["from"], {})[e["to"]] = e["weight"]
        adj.setdefault(e["to"], {})[e["from"]] = e["weight"]
        line_of.setdefault(e["to"], []).append((e["mode"] + ":" + e["from"], 1))
    line_of[HUB].append(("tram:" + HUB, 0))
    names = {s: [s] + data["aliases"].get(s, []) for s in adj}
    by_letter = {}
    for s, ns in names.items():
        for n in ns:
            if s not in by_letter.setdefault(n[0].upper(), []):
                by_letter[n[0].upper()].append(s)
    dist, prev = {}, {}
    for src in adj:
        d, p, pq = {src: 0}, {src: None}, [(0, src)]
        while pq:
            c, u = heapq.heappop(pq)
            if c > d[u]:
                continue
            for v, w in adj[u].items():
                if c + w < d.get(v, 1e9):
                    d[v], p[v] = c + w, u
                    heapq.heappush(pq, (c + w, v))
        dist[src], prev[src] = d, p
    return dict(adj=adj, dist=dist, prev=prev, by_letter=by_letter, names=names, line_of=line_of)


def path(net, a, b):
    out, p = [b], net["prev"][a]
    while out[-1] != a:
        out.append(p[out[-1]])
    return out[::-1]


def label(net, station, letter):
    """Name used for a letter: the alias that supplies the letter, if any."""
    for n in net["names"][station]:
        if n[0].upper() == letter:
            return n
    return station


# ---------------------------------------------------------------- optimiser
def candidates(net, letter, model):
    if model == "M2" and letter == "A":
        return [HUB]
    return net["by_letter"].get(letter, [])


def best_cost(net, text, model):
    """Exact minimum route cost for one line (fast path used by the controls)."""
    dist = net["dist"]
    states, penalty = {None: 0}, 0
    for ch in text:
        cands = candidates(net, ch, model)
        if not cands:
            penalty += SKIP_PENALTY
            continue
        new = {}
        for s in cands:
            best = None
            for p, c in states.items():
                if p == s:
                    continue
                v = c + (0 if p is None else dist[p][s])
                if best is None or v < best:
                    best = v
            if best is not None:
                new[s] = best
        if not new:  # e.g. AA under M2: no different station exists
            penalty += SKIP_PENALTY
            continue
        states = new
    return min(states.values()) + penalty


def k_best(net, text, model, k=10):
    """The k cheapest complete assignments for one line."""
    dist = net["dist"]
    states, penalty = {None: [(0, ())]}, 0
    for ch in text:
        cands = candidates(net, ch, model)
        if not cands:
            penalty += SKIP_PENALTY
            states = {p: [(c, seq + (None,)) for c, seq in lst] for p, lst in states.items()}
            continue
        new = {}
        for s in cands:
            pool = []
            for p, lst in states.items():
                if p == s:
                    continue
                step = 0 if p is None else dist[p][s]
                pool.extend((c + step, seq + (s,)) for c, seq in lst)
            pool.sort(key=lambda x: (x[0], x[1]))
            if pool:
                new[s] = pool[:k]
        if not new:
            penalty += SKIP_PENALTY
            states = {p: [(c, seq + (None,)) for c, seq in lst] for p, lst in states.items()}
            continue
        states = new
    allp = sorted((c + penalty, seq) for lst in states.values() for c, seq in lst)
    return allp[:k]


# ---------------------------------------------------------------- patterns
def describe(net, text, seq):
    stops = [(ch, s) for ch, s in zip(text, seq) if s is not None]
    legs = []
    for (c1, a), (c2, b) in zip(stops, stops[1:]):
        legs.append({"from": label(net, a, c1), "to": label(net, b, c2),
                     "cost": net["dist"][a][b], "via": path(net, a, b)})
    st = [s for _, s in stops]
    hub_returns = sum(1 for s in st[1:] if s == HUB)
    out_back = sum(1 for i in range(len(st) - 2) if st[i] == st[i + 2])
    # line sweeps: 3+ consecutive stops on one line with strictly monotone index
    sweeps = []
    for lid in {l for s in st for l, _ in net["line_of"][s]}:
        idx = [dict(net["line_of"][s]).get(lid) for s in st]
        i = 0
        while i < len(st):
            j = i
            while j + 1 < len(st) and idx[j] is not None and idx[j + 1] is not None:
                d0 = idx[j + 1] - idx[j]
                if d0 == 0:
                    break
                if j > i and (d0 > 0) != (idx[j] - idx[j - 1] > 0):
                    break
                j += 1
            if j - i + 1 >= 3:
                sweeps.append({"line": lid, "stops": [label(net, s, c) for c, s in stops[i:j + 1]]})
            i = max(j, i + 1)
    lines_touched = sorted({l for leg in legs for s in leg["via"] for l, _ in net["line_of"][s]
                            if all(l in dict(net["line_of"][x]) for x in leg["via"][:2])} or
                           {l for s in st for l, _ in net["line_of"][s]})
    return {"stops": [label(net, s, c) if s else f"[{c} unmatched]" for c, s in zip(text, seq)],
            "legs": legs, "hub_returns": hub_returns, "out_and_back": out_back,
            "line_sweeps": sweeps, "lines_touched": lines_touched}


# ---------------------------------------------------------------- tests
def variants():
    for choice in itertools.product(*[ax[2] for ax in VARIANT_AXES]):
        lines = {k: list(v) for k, v in LINES.items()}
        for (lid, pos, _), ch in zip(VARIANT_AXES, choice):
            lines[lid][pos] = ch
        yield "/".join(choice), {k: "".join(v) for k, v in lines.items()}


def percentile(obs, null):
    return (sum(1 for x in null if x <= obs) + 1) / (len(null) + 1)


def run_controls(net, lines, model, draws, rng):
    texts = list(lines.values())
    within, globl = [], []
    pool = list("".join(texts))
    lens = [len(t) for t in texts]
    for _ in range(draws):
        tot = 0
        for t in texts:
            l = list(t)
            rng.shuffle(l)
            tot += best_cost(net, "".join(l), model)
        within.append(tot)
        rng.shuffle(pool)
        tot, i = 0, 0
        for n in lens:
            tot += best_cost(net, "".join(pool[i:i + n]), model)
            i += n
        globl.append(tot)
    return within, globl


def per_line_within(net, text, model, draws, rng):
    null = []
    for _ in range(draws):
        l = list(text)
        rng.shuffle(l)
        null.append(best_cost(net, "".join(l), model))
    return null


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draws", type=int, default=10_000)
    ap.add_argument("--output", type=Path, default=OUTPUT)
    args = ap.parse_args()
    net = load_network()
    out = {"method": "docs/method/selected-stop-route-test.md", "seed": SEED, "draws": args.draws,
           "skip_penalty": SKIP_PENALTY, "network": str(NETWORK.relative_to(ROOT)),
           "letters_without_station": sorted(set("".join(LINES.values()) + "CGMSW") - set(net["by_letter"])),
           "models": {}}
    for model in ("M1", "M2"):
        res = {"variants": {}, "default": {}}
        for name, lines in variants():
            rng = random.Random(f"{SEED}-{model}-{name}")
            obs = {k: best_cost(net, t, model) for k, t in lines.items()}
            total = sum(obs.values())
            within, globl = run_controls(net, lines, model, args.draws, rng)
            res["variants"][name] = {
                "line_costs": obs, "total": total,
                "within_line_shuffle": {"pct_at_or_below": round(percentile(total, within), 4),
                                        "null_mean": round(sum(within) / len(within), 2),
                                        "null_min": min(within)},
                "global_shuffle": {"pct_at_or_below": round(percentile(total, globl), 4),
                                   "null_mean": round(sum(globl) / len(globl), 2)},
            }
        name, lines = next(variants())  # W/W/C/G default
        rng = random.Random(f"{SEED}-{model}-perline")
        for lid, text in list(lines.items()) + [CANCELLED]:
            null = per_line_within(net, text, model, args.draws, rng)
            routes = k_best(net, text, model, 10)
            res["default"][lid] = {
                "text": text, "cancelled": lid == CANCELLED[0],
                "best_cost": routes[0][0],
                "within_line_pct_at_or_below": round(percentile(routes[0][0], null), 4),
                "within_line_null_mean": round(sum(null) / len(null), 2),
                "routes": [dict(rank=i + 1, cost=c, **describe(net, text, seq))
                           for i, (c, seq) in enumerate(routes)],
            }
        out["models"][model] = res
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    for model, res in out["models"].items():
        v = res["variants"]["W/W/C/G"]
        ws = sorted(x["within_line_shuffle"]["pct_at_or_below"] for x in res["variants"].values())
        print(model, "default total", v["total"], v["line_costs"], "N1", v["within_line_shuffle"],
              "N2", v["global_shuffle"], "N1 range over 16", ws[0], ws[-1],
              "n<=0.10:", sum(1 for x in ws if x <= 0.10))
        for lid, d in res["default"].items():
            r = d["routes"][0]
            print(" ", lid, d["text"], d["best_cost"], "pct", d["within_line_pct_at_or_below"],
                  "null", d["within_line_null_mean"], " > ".join(r["stops"]))


if __name__ == "__main__":
    main()
