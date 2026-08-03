#!/usr/bin/env python3
"""Normalise extracted South Australian rail records for human review."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


FIELDS = [
    "station_id",
    "name",
    "historical_name",
    "mode",
    "line_or_system",
    "latitude",
    "longitude",
    "opened",
    "closed",
    "initials",
    "source_id",
    "confidence",
    "notes",
]


def normalise(value: str) -> str:
    return " ".join(value.strip().split())


def extract(source: Path, destination: Path) -> None:
    """Copy recognised fields into the canonical schema.

    This starter intentionally performs no OCR. Raw extractions should first be
    reviewed and supplied as a UTF-8 CSV with a header row.
    """
    with source.open(encoding="utf-8-sig", newline="") as src:
        reader = csv.DictReader(src)
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("w", encoding="utf-8", newline="") as dst:
            writer = csv.DictWriter(dst, fieldnames=FIELDS)
            writer.writeheader()
            for row in reader:
                writer.writerow({field: normalise(row.get(field, "")) for field in FIELDS})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path, default=Path("data/stations.csv"))
    args = parser.parse_args()
    extract(args.source, args.output)


if __name__ == "__main__":
    main()
