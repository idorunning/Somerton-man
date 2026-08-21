# Sequence and Connectivity Test — Design

**Status: not run. Blocked on `OPEN_QUESTIONS.md` items 1 and 3.**

This is the test that matters. Everything else in this repository either sets it up or works
around its absence.

## The question it answers

Set-membership asks: *does a place exist for each letter?* The answer is yes, for every letter,
which is why the answer is worthless — a random string would pass too.

The sequence test asks something a random string should fail: *read in written order, do the
letters trace a route a person could actually have travelled?*

A genuine itinerary has properties that a random string does not. Consecutive letters should
resolve to places that are connected — on the same line, on intersecting lines, or a short
walk apart. The route should not teleport. It should be traversable in a day, or in whatever
window the writer had. It should not require doubling back across the metropolitan area
between every pair of stops.

## The test

For each code line, in written order:

1. Enumerate every assignment of places to letters, subject to the constraint that place *i*
   begins with letter *i*.
2. For each assignment, evaluate the path *p₁ → p₂ → ... → pₙ* against the 1948 network:
   - Is each consecutive pair connected? Same route, interchange, or walkable gap.
   - What is the cumulative journey time using 1948 timetables where available, or a distance
     proxy where not?
   - How many mode changes and interchanges does it require?
3. Score each assignment. Retain the best-scoring path per line — the **best fit under
   sequence coherence**.
4. Compare the best fit for the real code lines against the best fit for a large sample of
   random strings of the same length drawn from the same letter distribution.

Step 4 is the whole test. If the real lines score no better than random strings, the hypothesis
fails a test it could have passed. If they score markedly better, that is the first genuine
evidence the itinerary reading has produced.

## What is needed to run it

**A network layer that does not yet exist.** The current locations table is a coordinate
gazetteer. It carries names, coordinates and map provenance. It carries no transport mode and
no connectivity.

Required additional columns:

| Column | Content |
|---|---|
| `mode` | rail, tram, trolleybus, motor bus, none |
| `route_id` | line or route identifier, repeatable per place |
| `route_seq` | ordinal position of the place along that route |
| `service_from` | earliest confirmed service date |
| `service_to` | closure date where applicable, else null |
| `source` | primary source for the above |

With `route_id` and `route_seq` populated, connectivity falls out for free: two places are
directly connected if they share a `route_id`, and interchange is a shared place across two
route identifiers.

## The fork

**Option A — proximity graph approximation.** Skip the network layer. Treat any two places
within a threshold distance as connected. Runnable immediately from existing coordinates.

Cheap, and it can still falsify: if the real lines score no better than random even under a
generous connectivity model, that is informative. But it can produce a false positive by
inventing connections that did not exist, and a false negative by imposing a uniform threshold
on a network whose density varied wildly between the inner suburbs and the outer routes.

**Option B — build the network layer.** Slower. Requires source work in Municipal Tramways
Trust records, railway working timetables and municipal bus route records. Produces a result
that means what it appears to mean.

**Assessment:** Option A is worth running as a pilot precisely because a negative under
generous assumptions would be a strong negative, and cheap. It should not be reported as the
test. If Option A returns anything other than a clean negative, Option B becomes necessary
before any claim is made.

## Scoring caution

The scoring function is where a hypothesis like this gets quietly rescued. Every free
parameter — walkable-gap threshold, interchange penalty, time budget — is an opportunity to
tune until the real lines outperform. Fix the parameters and the random-string baseline
*before* looking at how the real lines score, and record them in this document when set.
