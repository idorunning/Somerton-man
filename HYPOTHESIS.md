# The Hypothesis

## The claim

The five pencilled lines of capital letters found in the recovered Rubáiyát constitute a
travel itinerary. Each letter is the initial of a place.

A place means any of the following:

- a suburb or residential locality
- a country town
- a railway station on the South Australian Commissioner's Railways network
- a stop or terminus on the Glenelg tram
- a stop or terminus on a Municipal Tramways Trust or municipal motor bus route
- any named locality reachable from Adelaide by scheduled public transport in 1948

The itinerary is understood as places Carl Webb visited, or planned to visit, while searching
for Jessica Thomson at 90A Moseley Street, Glenelg.

## What this is not

**It is not a railway-station-only framework.** That was the starting frame and it was wrong.
A rail-only candidate pool leaves Q permanently unresolved, because Quorn is the sole Q-initial
station on the South Australian network and sits roughly 350 km from Adelaide — outside any
plausible search radius for a man looking for a woman in Glenelg. Widening the pool to
residential localities and bus-served suburbs resolves Q as Queenstown.

**It is not a geographically unbounded framework.** The candidate pool is Adelaide and its
reachable hinterland. A letter matching a place in Queensland is not a match.

**It is not a cipher hypothesis.** No claim is made here about substitution, one-time pads, or
any cryptographic construction. The claim is that the letters are mnemonic initials of place
names.

## The transcription

```
Line 1   W R G O A B A B D
Line 2   M L I A O I
Line 3   W T B I M P A N E T P
Line 4   M L I A B O A I A Q C   [commonly reported as struck through]
Line 5   I T T M T S A M S T G A B
```

This is the repository's standard working transcription, consistent with
`docs/hypothesis.md`. Character and strike-through variants must be frozen and recorded for
each analysis rather than silently resolved. The imported RPFA work excluded Line 2 on the
mistaken assumption that it was crossed out; those results require a sensitivity rerun using
the standard reading and a documented treatment of Line 4. Its relationship to Line 2 — the
shared `M L I A` opening — may still be relevant to how the writer worked.

Line 5 terminates `G A B`, read as Glenelg – Adelaide – Brighton.

## What rests on what

Carl Webb's identification via DNA in 2022 is the settled foundation of this work. Everything
else in this repository is layered inference above it and is treated as such.

The identification of the letters as an itinerary is inference.
The identification of any individual letter with any individual place is inference.
The search-for-Thomson motive is inference.

None of these are established. They are the hypothesis under test.

## The falsifiability problem

Every distinct letter in the standard transcription already has at least one
Adelaide-reachable candidate place. This was confirmed empirically, not assumed. The
consequence is that coverage tells us nothing: a random string of capitals drawn from the same
alphabet would also be fully coverable.

Set-membership analysis is therefore exhausted as a discriminating test. Only sequence and
connectivity can separate a genuine itinerary from noise — whether the letters, read in order,
trace a route that a person could actually have travelled on the 1948 network, in the order
written, in a plausible time.

That test has not been run. Its design is in `docs/method/sequence-test-design.md`. Its
blocking dependencies are in `OPEN_QUESTIONS.md`.

## The 19-month void

Webb's documented movements are absent between April 1947 and November 1948. The itinerary
hypothesis, if it holds, would place activity inside that window. The void is what makes the
hypothesis worth testing; it is not evidence for it.
