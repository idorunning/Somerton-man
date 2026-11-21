#!/usr/bin/env python3
"""Exploratory search-pattern analysis: hub excursions with at most one turnaround.

POST HOC. Written on 21 November 2026 after seeing the pre-registered result of
src/selected_stop_routes.py, which showed hub-and-spoke shapes in lines 1, 2 and 4.
Its outputs are candidates for checking against timetables, not findings.

Rule ("logical excursion"): read every A as Adelaide (North Terrace). That splits
each line into segments: hub-to-hub excursions, plus the open stretches before the
first A and after the last A. Inside a segment, the traveller rides shortest paths
between stops and may reverse direction at most once (one turnaround), so each
segment is a single out-and-back or a one-way sweep. Unmatched letters (Q) are
skipped.

For each segment it lists every station assignment that satisfies the rule, ranked
by travel cost, and it measures how often within-line shuffles of the same letters
can also be read this way.
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

from selected_stop_routes import (CANCELLED, HUB, LINES, ROOT, SEED, label, load_network, path)

OUTPUT = ROOT / "data/processed/logical-excursions-2026-11-21.json"
MAX_TURNS = 1


def segments(text):
    """Split at A. Returns (letters, starts_at_hub, ends_at_hub)."""
    parts = text.split("A")
    out = []
    for i, p in enumerate(parts):
        out.append((p, i > 0, i < len(parts) - 1))
    return out


def solutions(net, letters, start_hub, end_hub, limit=None):
    """All assignments for one segment with <= MAX_TURNS turnarounds."""
    letters = [c for c in letters if net["by_letter"].get(c)]
    found = []

    def walk_turns(seq):
        nodes = [seq[0]]
        for a, b in zip(seq, seq[1:]):
            nodes += path(net, a, b)[1:]
        return sum(1 for i in range(1, len(nodes) - 1) if nodes[i - 1] == nodes[i + 1])

    def rec(seq):
        if limit and len(found) >= limit:
            return
        stops = ([HUB] if start_hub else []) + seq
        if len(stops) >= 2 and walk_turns(stops) > MAX_TURNS:
            return
        if len(seq) == len(letters):
            full = stops + ([HUB] if end_hub else [])
            if len(full) >= 2 and (full[-1] == full[-2] or walk_turns(full) > MAX_TURNS):
                return
            cost = sum(net["dist"][a][b] for a, b in zip(full, full[1:]))
            found.append((cost, tuple(seq)))
            return
        for s in net["by_letter"][letters[len(seq)]]:
            prev = seq[-1] if seq else (HUB if start_hub else None)
            if s != prev:
                rec(seq + [s])

    if not letters:
        return [(0, ())]
    rec([])
    return sorted(found)


def line_feasible(net, text):
    return all(solutions(net, seg, s, e, limit=1) for seg, s, e in segments(text))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draws", type=int, default=2000)
    args = ap.parse_args()
    net = load_network()
    out = {"status": "exploratory, post hoc", "rule": __doc__.strip(), "lines": {}}
    rng = random.Random(f"{SEED}-excursions")
    for lid, text in list(LINES.items()) + [CANCELLED]:
        segs = []
        for seg, s, e in segments(text):
            sols = solutions(net, seg, s, e)
            segs.append({
                "segment": ("A " if s else "") + " ".join(seg) + (" A" if e else ""),
                "n_logical_readings": len(sols),
                "top": [{"cost": c,
                         "stops": (["Adelaide"] if s else []) +
                                  [label(net, st, ch) for st, ch in zip(seq, [x for x in seg if net["by_letter"].get(x)])] +
                                  (["Adelaide"] if e else [])}
                        for c, seq in sols[:8]],
            })
        hits = 0
        for _ in range(args.draws):
            l = list(text)
            rng.shuffle(l)
            hits += line_feasible(net, "".join(l))
        out["lines"][lid] = {"text": text, "cancelled": lid == CANCELLED[0],
                             "every_segment_logical": all(x["n_logical_readings"] for x in segs),
                             "shuffles_every_segment_logical": round(hits / args.draws, 4),
                             "segments": segs}
        print(lid, text, "real feasible:", out["lines"][lid]["every_segment_logical"],
              "shuffle rate:", out["lines"][lid]["shuffles_every_segment_logical"])
        for x in segs:
            print("   ", x["segment"], x["n_logical_readings"],
                  [" > ".join(t["stops"]) + f" ({t['cost']})" for t in x["top"][:3]])
    OUTPUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
