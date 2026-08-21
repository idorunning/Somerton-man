# Radial Proximity Frequency Analysis (RPFA)

## What it does

RPFA asks a geometric question: given a candidate centre point, how large a radius is needed
before every letter in the code has at least one matching place inside it?

The output for any centre is a single number — the minimum covering radius — plus the identity
of the place that forced it. That place is the **binding constraint**: the letter whose nearest
candidate sits furthest out.

Ranking every candidate centre by minimum covering radius produces a league table. A centre
that covers the whole alphabet tightly is a better fit for an itinerary written by someone
working out of that location than a centre that needs to reach halfway across the state.

## Procedure

1. Take the candidate place pool from `data/processed/localities.csv`.
2. Take the distinct letters of the frozen transcription variant (see below).
3. For each candidate centre *c*:
   - For each letter *L*, find the nearest place in the pool whose name begins with *L*.
     Record the great-circle distance.
   - The minimum covering radius for *c* is the maximum of those per-letter distances.
   - The binding constraint for *c* is the letter and place that produced that maximum.
4. Rank all centres ascending by minimum covering radius.

## Decisions baked into the method

**Transcription treatment must be declared per run.** The standard working transcription uses
W at the start of Lines 1 and 3 and records Line 4, `MLIABOAIAQC`, as commonly reported
crossed out. The imported historical RPFA work excluded Line 2 instead. That was based on an
incorrect transcription and must be retained only as a labelled legacy variant. A corrected
run should pre-declare whether Line 4 is excluded, included as an abandoned plan, or analysed
both ways — see `OPEN_QUESTIONS.md` items 2 and 6.

**Great-circle distance, not travel distance.** RPFA is deliberately a geometric test, not a
network test. It measures spatial plausibility only. It says nothing about whether the places
were connected, or reachable in sequence, or reachable at all. That is the sequence test's job
and it is a different question.

**First letter only.** A place matches a letter if the place name's first letter matches. No
partial matching, no phonetic matching, no matching on second words. "Port Adelaide" matches P,
not A.

## What RPFA can and cannot tell you

It can tell you that a proposed anchor point is spatially awkward — that reading the code as an
itinerary written from location X requires X to reach much further than most alternatives do.
That is a real result and it is what the residential frame produced for 90A Moseley Street.

It cannot tell you the hypothesis is true. Coverage is not discrimination. See
`docs/findings/set-membership-analysis.md`.

## Sensitivity

Two parameters move the results and both are choices rather than findings:

- **Candidate pool composition.** Transport stops and residential localities give materially
  different answers. Both frames are documented; neither is privileged.
- **Population threshold.** The residential frame toggles between ≥500 and ≥1,000 persons.
  Threshold stability has not been tested — see `OPEN_QUESTIONS.md` item 5.
