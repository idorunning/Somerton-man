#!/usr/bin/env python3
"""Starter framework for route-pattern fit and alternatives analysis."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Candidate:
    token: str
    station_id: str
    historical_validity: float
    geographic_continuity: float
    timetable_feasibility: float
    pattern_economy: float
    repetition_fit: float
    source_quality: float
    alternative_density: float


def score(candidate: Candidate) -> float:
    """Return an unvalidated baseline score on a 0–1 scale.

    Weights are deliberately equal until the methodology and validation set are
    agreed. Alternative density is treated as a penalty.
    """
    positive = (
        candidate.historical_validity
        + candidate.geographic_continuity
        + candidate.timetable_feasibility
        + candidate.pattern_economy
        + candidate.repetition_fit
        + candidate.source_quality
    ) / 6
    penalty = max(0.0, min(1.0, candidate.alternative_density))
    return max(0.0, min(1.0, positive * (1 - penalty)))


if __name__ == "__main__":
    raise SystemExit("Import this module from an analysis script or test.")
