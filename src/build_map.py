#!/usr/bin/env python3
"""Build map-ready station data from the canonical CSV."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def build_geojson(source: Path) -> dict:
    features = []
    with source.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if not row.get("latitude") or not row.get("longitude"):
                continue
            features.append(
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [float(row["longitude"]), float(row["latitude"])],
                    },
                    "properties": {
                        key: value
                        for key, value in row.items()
                        if key not in {"latitude", "longitude"}
                    },
                }
            )
    return {"type": "FeatureCollection", "features": features}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path("data/stations.csv"))
    parser.add_argument("--output", type=Path, default=Path("app/stations.geojson"))
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(build_geojson(args.input), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
