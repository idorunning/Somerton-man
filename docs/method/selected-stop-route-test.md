# Selected-stop rail route test — pre-registration

**Written:** 21 November 2026, before any real code line was scored under this model.
**Status at writing:** not run. Results go in `docs/findings/selected-stop-routes-2026-11-21.md`.

## Why this test

Nathan's working theory is that the retained lines are shorthand for rail journeys, a route
record or route plan made by Carl Webb while looking for Jessica Thomson. The September audit
tested only the strictest version: each line as an unbroken run of consecutive station initials
on four corridors. That failed (0 of 256). It did not test the version a searcher would
actually write down: the stations he **got off at**, in order, skipping the ones he rode
through.

This test asks a question the earlier work could not: **is the written order of the letters
more route-like than the same letters in a random order?** A logical searcher would write a
route that moves efficiently along lines, returns to a hub, or sweeps a line station by
station. A shuffled string has the same letters but no such order. If the real lines need no
less travel than their own shuffles, order carries no route signal under this model.

## Fixed inputs

- **Network:** `data/reference/sar-metro-1938-network.json`, transcribed on 21 November 2026
  from the PP No. 47 metropolitan inset (96 rail stations, 10 lines) plus one tram edge,
  Adelaide to Glenelg, weight 8. Station names as printed. Two aliases: North Terrace may be
  read as Adelaide (A) and Commercial Rd as Port Adelaide (P).
- **Transcription:** retained physical lines 1, 3, 4 and 5. Sixteen readings: W/M at the start
  of lines 1 and 3, C/S at the end of line 4, G/C before the final AB of line 5. Default
  W/W/C/G. Cancelled line 2 (`MLIAOI`) is scored separately and never pooled.
- **Matching:** first letter of the station name or alias. No second-word matching, no
  phonetic matching.

## Model

Each letter is a station where the traveller stopped. Between consecutive stops he rides the
shortest path through the network.

- **Leg cost:** shortest-path weight, rail edge = 1 per station hop, tram edge = 8.
- **Consecutive stops must differ.** Writing the same station twice in a row is not a journey.
- **A letter with no station** (Q in the rail-only network) is skipped with a fixed penalty of
  12. The route continues from the previous stop to the next one.
- **Line score:** the minimum total cost over all assignments of stations to letters,
  found exactly by dynamic programming.
- **Overall score:** the sum of the four retained line scores.

Two variants, both declared now:

- **M1 free:** every letter may be any matching station.
- **M2 Adelaide hub:** every A must be Adelaide (North Terrace). This is the "search out of
  the city and come back" reading of a man based in town.

## Controls

10,000 draws each, seed `19481130`, identical optimiser for every draw:

- **N1 within-line shuffle.** Letters shuffled inside each line. Same letters per line, order
  destroyed. **This is the main test of letter order.**
- **N2 global shuffle.** All 44 retained letters shuffled across lines of length 9, 11, 11
  and 13, as in the September repetition test.

Reported figure: the share of shuffles with a total cost **at or below** the real one, with
the (k + 1)/(n + 1) correction. Small = the real order is more route-like than chance.

## What counts as a result

- Overall percentile at or below **5%** under N1 for the default reading, and at or below 10%
  for at least 12 of the 16 readings: the order carries a route-like signal under this model.
  Evidence for the model, not for Webb, motive or date.
- Overall percentile above **20%** under N1: the written order is no more route-like than
  chance on the 1938 metropolitan rail network. That counts against the selected-stop rail
  reading. It does not rule out a multimodal or non-metropolitan reading.
- Anything between is inconclusive and is reported as such.

Per-line percentiles are descriptive. With four lines and two models, one line under 5% is
not a discovery on its own.

## Descriptive outputs (not tests)

For the default reading and both models: the ten cheapest routes per line, with each leg's
path, and pattern labels for the best route:

- **hub returns:** legs that end at Adelaide;
- **line sweeps:** runs of three or more stops moving one way along a single line;
- **out-and-back:** X → Y → X;
- **lines touched.**

These describe what the best fit looks like. They are chosen by the optimiser after seeing
the letters, so they are candidates, not findings.

## Known limits, accepted in advance

- 1938 infrastructure, not a 1948 timetable.
- Metropolitan inset only. Country stations (Gawler, Murray Bridge, Quorn and so on) are out.
- No interchange penalty, fares or times.
- The tram weight of 8 is a judgement. It affects only legs touching Glenelg.
