# Finding — Selected-stop rail routes and search patterns

**Date:** 21 November 2026
**Verdict: inconclusive under the pre-registered rule. The written order of the letters is
somewhat more route-like than shuffled order on the 1938 metropolitan rail network (10–14% of
shuffles do as well for the default reading; 6–26% across all 16 readings), but it misses the
5% threshold set in advance. The signal, such as it is, sits in physical lines 1 and 4 and in
the cancelled line 2, which share a hub-and-spoke shape. Lines 3 and 5 look like chance.**

Method fixed in advance: [`docs/method/selected-stop-route-test.md`](../method/selected-stop-route-test.md).
Code: `src/selected_stop_routes.py` (pre-registered), `src/logical_excursions.py` (exploratory,
written after seeing the first result). Outputs: `data/processed/selected-stop-routes-2026-11-21.json`,
`data/processed/logical-excursions-2026-11-21.json`.

## What was new in this test

1. **A transcribed network.** The 1938 PP No. 47 metropolitan inset was read station by station
   from the repository photographs (`090410593`, `090419827`) into
   `data/reference/sar-metro-1938-network.json`: 96 rail stations on 10 lines, from Outer
   Harbour to Willunga and Balhannah, plus the Adelaide–Glenelg tram. This is the first
   machine-readable network in the repository. It shows infrastructure in 1938, not a 1948
   timetable.
2. **The model a searcher would write.** Each letter is a station he got off at; between
   stops he rides the shortest path. The September audit tested only unbroken runs of
   consecutive stations.
3. **Letter order tested directly.** The same optimiser was run on 10,000 within-line
   shuffles. If order carried no route information, the real lines would sit in the middle
   of that distribution.

## Pre-registered result

Total travel cost is the number of station hops ridden across the four retained lines,
minimised over every possible station assignment. Lower is more compact.

| Model | Real total | Shuffle mean | Shuffles at or below real (within-line) | Global shuffle |
|---|---:|---:|---:|---:|
| M1, any matching station | 210 | 232.7 | **14.1%** | 17.4% |
| M2, every A is Adelaide | 222 | 251.2 | **10.3%** | 8.4% |

Across the 16 readings, the within-line figure ranges from 5.9% to 25.7% (M1) and 5.9% to
23.4% (M2). No reading reaches 5%. Readings with M at the start of line 3 (W/M/…) come
closest; readings with M at the start of line 1 are weakest. Under the rule set in advance,
this is **inconclusive**. It is not a negative, because it does not exceed 20%.

### Line by line (default reading, descriptive only)

| Physical line | Letters | Best cost | Shuffle mean | Shuffles as good, M1 | M2 |
|---|---|---:|---:|---:|---:|
| 1 | WRGOABABD | 25 | 33.7 | 6.9% | 5.0% |
| 2 (cancelled) | MLIAOI | 23 | 31.5 | 8.3% | 5.8% |
| 3 | WTBIMPANETP | 61 | 61.5 | 51.5% | 77.5% |
| 4 | MLIABOAIAQC | 46 | 55.4 | 7.3% | 4.1% |
| 5 | ITTMTSAMSTGAB | 78 | 82.6 | 39.8% | 33.0% |

Four lines and two models make eight looks; one or two near 5% is what chance alone would
often produce. The pattern is worth following, not claiming.

## The search patterns the letters allow

The best fits for lines 1, 2 and 4 are **hub-and-spoke**: the traveller keeps returning to
Adelaide between short excursions. That prompted an exploratory check (post hoc, so treat
it as candidate generation): read every A as Adelaide and ask which stations give each
excursion **at most one turnaround**, so it is a single out-and-back or a one-way sweep,
which is what a methodical man would plan.

Ranked by how tightly the letters constrain the route:

| Rank | Fragment | Logical readings | Best reading | Why it ranks here |
|---|---|---:|---|---|
| 1 | Line 5, `A M S T G A` | **4** | Adelaide → Mile End (or Millswood / Mitcham) → Sleep's Hill → Torrens Park → Goodwood → Adelaide | Only the Hills line works. Out to Sleep's Hill, then back towards town stopping at Torrens Park and Goodwood, in station order. The G here is Goodwood, not Glenelg. |
| 2 | Line 4, `A I A` | **1** | Adelaide → Islington → Adelaide | Islington is the only I station. Fixed, but a one-letter excursion says little. |
| 3 | Line 4, `A B O A` | 9 | **Adelaide → Brighton → Oaklands → Adelaide** | Out to Brighton, back stopping at Oaklands: the only reading where B and O are on one line in homeward order. Matches the website's ABOAIA candidate independently. Brighton is the nearest station to Moseley Street, Glenelg. Next best (Belair → Overway Bridge) costs 70% more. |
| 4 | Line 1, `W R G O A` | 22 | Wingfield → Rosewater → Glanville → Ovingham → Adelaide | A loop: round the Dry Creek–Port line to the Port, then home by the north line. The letters W-R-G follow the stations in running order. |
| 5 | Line 1, `A B A B` | 8 | Adelaide ↔ Bowden, twice | The shape (two trips to the same B) is clear; which B is not. Bowden is cheapest, Brighton second, then Brighton Parade, Blackwood and Belair. |
| 6 | Line 3, `A N E T P` | 12 | Adelaide → North Adelaide → Ethelton → Taperoo → Peterhead | A Port/Outer Harbour excursion, but weak. |
| — | Line 3, `W T B I M P` and line 5, `I T T M T S` | **0** | none | No reading with one turnaround exists. The double T is the main obstacle: Torrens Park and Taperoo are the only T stations and sit on opposite sides of the city. |
| — | Line 4, `Q` | none | none | No Q station on the metropolitan rail network. A rail reading of `…AQC` needs either Quorn (about 300 km away) or a non-rail Q such as Queenstown by bus. |

How often shuffled versions of each line can also be read this way: line 1, 82%; line 4,
50%; cancelled line 2, 54%; line 3, 26%; line 5, 8%. So a logical reading of line 1 is not
surprising, and lines 3 and 5 fail as wholes.

### What a rail search plan would look like on this reading

If line 4 and the middle of line 5 are route notes, they describe **day trips out of the
city, one radial line at a time, stopping at stations in running order on the way back**:

- Brighton line: out to Brighton, back via Oaklands (line 4).
- North line: Islington and back (line 4).
- Hills line: out to Sleep's Hill, back via Torrens Park and Goodwood (line 5).
- Possibly the Port loop: Wingfield, Rosewater, Glanville, home via Ovingham (line 1).

That is a logical way to search suburbs from a city base. It is also what any short string of
common initials can be made to resemble, which is why the controls matter more than the
stories.

## What this does and does not show

- It does **not** show that the letters are a route, that Webb wrote them, or that he was
  looking for Jessica Thomson. Only one fragment (Brighton) touches the Glenelg corridor, and
  the G of `GAB` fits a logical route better as Goodwood than as Glenelg.
- The strict consecutive-station reading stays rejected (September audit). The
  selected-stop reading is **not rejected** and is **not supported** at the threshold set.
- Lines 1 and 4 carry whatever route-like order exists. Line 2 (cancelled) behaves like line
  4, consistent with a false start of the same plan.
- Lines 3 and 5 do not read as single logical rail trips. If they are route notes, they need
  another mode, another area, or a different rule for repeated letters.

## Limits

- 1938 map, not a 1948 timetable. Some stations may have lost passenger stops by 1948.
- Station order marked "medium" in the network file (Hills line beyond Belair, Semaphore and
  Dry Creek–Port junctions) should be checked against a working timetable.
- Cost is station hops. It favours inner stations such as Bowden, so "cheapest" is not the
  same as "most likely". Where the shape is clear but the station is not (`ABAB`), all
  alternatives are listed in the JSON.
- The excursion rule and its ranking were devised after the first result. They are for
  choosing what to check, not evidence.
- Metropolitan rail and one tram only. Buses, country lines and walking are not modelled.

## Next steps this points to

1. Check the Hills line, Brighton line and north line stopping patterns in a 1947–48 SAR
   working timetable. If Sleep's Hill, Torrens Park, Oaklands or Islington had no passenger
   stop, the best readings fall.
2. Add bus routes (Queenstown first) and rerun the same test with the same thresholds, as a
   separate model.
3. Freeze a period prose and verse initial corpus and run it through the same optimiser, to
   see whether ordinary English initials look equally "route-like".
