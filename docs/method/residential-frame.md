# The Residential Locality Frame

## Why the frame changed

The candidate pool started as railway stations, then widened to all transport stops across
rail, tram and motor bus. Both frames share a flaw: they define the pool by *infrastructure*
rather than by *destination*.

A man searching for a woman is not travelling to a stop. He is travelling to a place where
people live. A tram stop in the middle of parkland and a suburb of four thousand people are
not equivalent candidates, but a stop-based pool treats them identically — and it silently
weights the pool towards wherever the network happened to be dense, which in 1948 Adelaide
means the inner west and the Glenelg corridor.

The residential frame rebuilds the pool from population instead.

## Source

1947 Commonwealth Census, Volume I, Part VIII. Metropolitan municipality totals extracted for
all Adelaide-area local government areas.

Extraction was by `pdftotext` with OCR-tolerant numeric parsing. Every row was reconciled
against its male-plus-female column sum before acceptance; the full set of metropolitan
municipality totals reconciled exactly. That reconciliation is the quality gate and it should
be reapplied on any re-extraction.

Note the year mismatch: 1947 census data used to reason about 1948 conditions. One year is
tolerable. It is recorded here so it is not forgotten.

## Threshold

The pool uses a dual threshold toggle rather than a fixed cut-off:

- **≥500 persons** — inclusive, admits small localities
- **≥1,000 persons** — restrictive, admits only substantial suburbs

Neither figure is principled. They are round numbers chosen to bracket a plausible range. The
toggle exists precisely so the threshold is visible as a choice rather than hidden as an
assumption. Whether the headline results are stable across the two settings has not been
tested; see `OPEN_QUESTIONS.md` item 5.

## What the frame changed

Under the transport-stop frame, the Glenelg corridor sits in a dense part of the network and
an anchor at Moseley Street reads as reasonably central.

Under the residential frame, it does not. 90A Moseley Street requires a 14.39 km covering
radius and ranks 111th of 161 candidate centres — the bottom third. The tightest lens anywhere
is 5.40 km, near West Croydon.

That is not a falsification. A man can perfectly well write an itinerary from a spatially
awkward starting point, and if he was travelling *out* from Glenelg to search, awkwardness is
what you would expect. But it removes an argument that was previously doing quiet work: the
idea that Moseley Street sits naturally at the centre of the code's geography. It does not.

## Reproducing it

The interactive tool `tools/rpfa-residential-frame.html` implements this frame with a
draggable lens on an SVG map, a centre ranking table, and data, sources and method tabs. It is
currently missing from the repository — see `OPEN_QUESTIONS.md` item 4.
