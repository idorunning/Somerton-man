#!/usr/bin/env python3
"""Reproduce the bounded four-corridor review with the Python standard library.

Run from any working directory:
    python3 /path/to/somerton-man/src/review_route_sequences.py --self-test

The default input and output paths resolve relative to this script's repository,
not the caller's working directory. Explicit relative paths resolve from the caller.
The JSON output is deterministic for identical input bytes and script bytes.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import string


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/reference/route-sequence-inputs.json"
DEFAULT_OUTPUT = ROOT / "data/processed/route-sequence-review-2026-09-05.json"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def validate_inputs(data: dict) -> None:
    active = data["active_lines"]
    if len({line["id"] for line in active}) != len(active):
        raise ValueError("Active line IDs must be unique")
    if data["cancelled_line"]["id"] in {line["id"] for line in active}:
        raise ValueError("Cancelled line must remain separate from active lines")
    if len({route["id"] for route in data["routes"]}) != len(data["routes"]):
        raise ValueError("Route IDs must be unique")
    values = [line["text"] for line in active + [data["cancelled_line"]]]
    values += [route["sequence"] for route in data["routes"]]
    if any(not value or any(c not in string.ascii_uppercase for c in value) for value in values):
        raise ValueError("Sequences must be non-empty, unspaced ASCII capital letters")
    line_by_id = {line["id"]: line["text"] for line in active}
    positions = set()
    for axis in data["variant_axes"]:
        line = line_by_id[axis["line_id"]]
        index = axis["index"]
        if not -len(line) <= index < len(line):
            raise ValueError("Variant index is outside its line")
        position = (axis["line_id"], index % len(line))
        if position in positions:
            raise ValueError("Variant axes must refer to distinct positions")
        positions.add(position)
        choices = axis["choices"]
        if not choices or len(set(choices)) != len(choices):
            raise ValueError("Variant choices must be non-empty and unique")
        if any(len(c) != 1 or c not in string.ascii_uppercase for c in choices):
            raise ValueError("Variant choices must be single ASCII capital letters")


def compare(code: str, route: str) -> dict:
    """Longest common substring using independent start positions and no gaps."""
    longest = 0
    overlaps = []
    full_matches = []
    for start in range(len(route) - len(code) + 1):
        if route.startswith(code, start):
            full_matches.append(start)
    for code_start in range(len(code)):
        for route_start in range(len(route)):
            length = 0
            while (code_start + length < len(code)
                   and route_start + length < len(route)
                   and code[code_start + length] == route[route_start + length]):
                length += 1
            if length > longest:
                longest, overlaps = length, []
            if length and length == longest:
                overlaps.append({
                    "text": code[code_start:code_start + length],
                    "code_start": code_start,
                    "route_start": route_start,
                    "code_position": code_start + 1,
                    "route_position": route_start + 1,
                })
    return {
        "full_line_match": bool(full_matches),
        "full_line_match_route_starts": full_matches,
        "longest_overlap_length": longest,
        "longest_overlaps": overlaps,
    }


def comparisons(lines: list[dict], routes: list[dict]) -> list[dict]:
    records = []
    for route in routes:
        for direction in ("forward", "reverse"):
            sequence = route["sequence"] if direction == "forward" else route["sequence"][::-1]
            for line in lines:
                record = {
                    "route_id": route["id"], "route_label": route["label"],
                    "direction": direction, "oriented_route_sequence": sequence,
                    "line_id": line["id"], "physical_line": line["physical_line"],
                    "code_text": line["text"], **compare(line["text"], sequence),
                }
                for overlap in record["longest_overlaps"]:
                    start, length = overlap["route_start"], len(overlap["text"])
                    positions = range(start, start + length)
                    overlap["original_route_positions"] = [
                        pos + 1 if direction == "forward" else len(sequence) - pos
                        for pos in positions
                    ]
                records.append(record)
    return records


def summarise_routes(records: list[dict], routes: list[dict]) -> list[dict]:
    result = []
    for route in routes:
        group = [record for record in records if record["route_id"] == route["id"]]
        longest = max(record["longest_overlap_length"] for record in group)
        result.append({
            "route_id": route["id"], "route_label": route["label"],
            "full_line_matching_comparisons": sum(record["full_line_match"] for record in group),
            "longest_overlap_length": longest,
            "longest_overlap_texts": sorted({
                overlap["text"] for record in group
                if record["longest_overlap_length"] == longest
                for overlap in record["longest_overlaps"]
            }),
        })
    return result


def analyse(data: dict, input_bytes: bytes) -> dict:
    validate_inputs(data)
    variants = []
    for choices in itertools.product(*(axis["choices"] for axis in data["variant_axes"])):
        characters = {line["id"]: list(line["text"]) for line in data["active_lines"]}
        for axis, character in zip(data["variant_axes"], choices):
            characters[axis["line_id"]][axis["index"]] = character
        lines = [{**line, "text": "".join(characters[line["id"]])} for line in data["active_lines"]]
        combined = "".join(line["text"] for line in lines)
        records = comparisons(lines, data["routes"])
        variants.append({
            "id": "/".join(choices),
            "readings": dict(zip((axis["id"] for axis in data["variant_axes"]), choices)),
            "active_lines": lines, "active_character_count": len(combined),
            "distinct_active_character_count": len(set(combined)),
            "distinct_active_characters": "".join(sorted(set(combined))),
            "active_character_frequencies": dict(sorted(Counter(combined).items())),
            "characters_including_cancelled_line": len(combined) + len(data["cancelled_line"]["text"]),
            "comparison_count": len(records),
            "full_line_matching_comparisons": sum(record["full_line_match"] for record in records),
            "route_summary": summarise_routes(records, data["routes"]), "comparisons": records,
        })
    default = next((variant for variant in variants if variant["id"] == data["default_variant"]), None)
    if default is None:
        raise ValueError("Default variant does not occur in the variant axes")
    cancelled_records = comparisons([data["cancelled_line"]], data["routes"])
    return {
        "schema_version": 1, "review_date": data["review_date"], "title": data["title"],
        "reproducibility": {
            "input_sha256": sha256(input_bytes),
            "script_sha256": sha256(Path(__file__).read_bytes()),
            "generator": "src/review_route_sequences.py", "dependencies": "Python 3 standard library",
            "time_policy": "Fixed review date from input; no wall-clock timestamp",
        },
        "provenance": data["provenance"], "method": data["method"], "caveats": data["caveats"],
        "scope": {"route_count": len(data["routes"]), "routes": data["routes"],
                  "active_physical_lines": [line["physical_line"] for line in data["active_lines"]],
                  "variant_axes": data["variant_axes"], "default_variant": data["default_variant"]},
        "summary": {
            "variant_count": len(variants), "route_direction_count": 2 * len(data["routes"]),
            "active_character_count": default["active_character_count"],
            "characters_including_cancelled_line": default["characters_including_cancelled_line"],
            "default_distinct_active_character_count": default["distinct_active_character_count"],
            "active_comparison_count": sum(variant["comparison_count"] for variant in variants),
            "active_full_line_matching_comparisons": sum(variant["full_line_matching_comparisons"] for variant in variants),
            "default_route_summary": default["route_summary"],
            "interpretation": "Descriptive exact-string comparison limited to the four supplied prior corridor transcriptions; no conclusion about all possible itineraries or the full 1948 network follows.",
        },
        "variants": variants,
        "cancelled_line_separate": {
            "line": data["cancelled_line"], "character_count": len(data["cancelled_line"]["text"]),
            "comparison_count": len(cancelled_records),
            "full_line_matching_comparisons": sum(record["full_line_match"] for record in cancelled_records),
            "route_summary": summarise_routes(cancelled_records, data["routes"]),
            "comparisons": cancelled_records,
        },
    }


def self_test() -> None:
    """Check no-gap semantics, direction, tied positions and review invariants."""
    # An independent set-of-substrings oracle checks longest-overlap lengths.
    examples = [("", ""), ("AB", "AXBY"), ("ABC", "CBA"),
                ("AB", "ABAB"), ("Q", "AAAA"), ("ABCD", "BC")]
    for code, route in examples:
        expected = max((end - start for start in range(len(code))
                        for end in range(start + 1, len(code) + 1)
                        if code[start:end] in route), default=0)
        actual = compare(code, route)
        assert actual["longest_overlap_length"] == expected, (code, route)
    assert not compare("AB", "AXBY")["full_line_match"], "Subsequence must not count as contiguous"
    assert not compare("ABC", "CBA")["full_line_match"]
    assert compare("ABC", "CBA"[::-1])["full_line_match"]
    assert compare("AB", "ABAB")["full_line_match_route_starts"] == [0, 2]
    assert len(compare("AB", "ABAB")["longest_overlaps"]) == 2
    payload = DEFAULT_INPUT.read_bytes()
    output = analyse(json.loads(payload), payload)
    summary = output["summary"]
    assert summary["variant_count"] == 8
    assert summary["active_character_count"] == 44
    assert summary["characters_including_cancelled_line"] == 50
    assert summary["default_distinct_active_character_count"] == 17
    assert summary["active_comparison_count"] == 256
    assert summary["active_full_line_matching_comparisons"] == 0
    assert [route["longest_overlap_length"] for route in summary["default_route_summary"]] == [2, 2, 2, 1]
    mmc = next(variant for variant in output["variants"] if variant["id"] == "M/M/C")
    assert mmc["distinct_active_character_count"] == 16
    assert output["cancelled_line_separate"]["comparison_count"] == 8
    assert output["cancelled_line_separate"]["full_line_matching_comparisons"] == 0
    assert all(record["line_id"] != "L2" for variant in output["variants"] for record in variant["comparisons"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--self-test", action="store_true", help="Run semantic and fixed-review checks before generating output")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    payload = args.input.read_bytes()
    output = analyse(json.loads(payload), payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output.resolve()), "self_test": "passed" if args.self_test else "not requested", **output["summary"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
