# Prior artefacts recovered from private project storage

Two documents recovered on 21 August 2026 from the private extractor-output folder. Both
predate this repository and neither has a producing script here. Account details and storage
identifiers are deliberately omitted from this public repository.

They are filed as historical artefacts, not as current findings. Read the reconciliation below
before citing either of them.

| File | Original | Date |
|---|---|---|
| `queenstown_analysis_2026-04-28.md` | `queenstown_analysis.md` | 28 April 2026 |
| `rpfa_marino_summary_2026-04-29.md` | `rpfa/summary.md` | 29 April 2026 |

---

## Reconciliation 1: the Queenstown document contradicts the project record

`queenstown_analysis_2026-04-28.md` concludes:

> Queenstown **is** on the 1938 SA Railways map, on the Adelaide–Port Adelaide main line, read
> at **high confidence from two independent images**.

The session of 29 April 2026 concluded the opposite: that Queenstown was never an SA Railways
station, and was served by the Port Adelaide tramway — horse trams from 1882, electrified
1917, closed July 1935 — followed by motor bus and trolleybus from 1935 and 1938.

These cannot both be right. Three things about the Queenstown document weaken it:

**It was not reading PP No. 47.** The two images it processed were
`PXL_20251014_202643575.jpg` and `Queenstowns capture.png`. Neither is among the twenty
PP No. 47 scans in `data/raw/maps/1938-sa-railways/`. The document itself describes the wide
image as "an Adelaide-environs street-and-rail map" — a street map showing rail, not the
Railways Commissioner's schedule. A street map may well label a suburb called Queenstown
without that suburb having a station.

**It explains away its own contradicting evidence.** The extraction pipeline flagged Queenstown
as absent from the canonical station list built from PP No. 47. The document dismisses this as
a false positive of the fuzzy matcher. The dismissal is backwards: absence from the
PP47-derived list is precisely the evidence that Queenstown was not a station on that map, and
the document even concedes in passing that "Queenstown may not have been a named station stop"
there.

**High confidence is a reading-confidence score, not a historical one.** Two vision passes
agreeing that a label says "Queenstown" establishes that the label says Queenstown. It
establishes nothing about what kind of place the label marks.

**Status:** the 29 April tramway-and-bus account is the better-sourced of the two and should be
treated as current until a primary record settles it. The rail claim in this document should
not be cited. See `OPEN_QUESTIONS.md` item 1.

Two source images referenced by this document — the `PXL_20251014_*` wide view and
`Queenstowns capture.png` — are not in this repository and not in Drive. If they exist locally
they should be added to `data/raw/maps/`, because a document citing images nobody can see is
not evidence.

---

## Reconciliation 2: the Marino result uses a baseline that flatters it

`rpfa_marino_summary_2026-04-29.md` reports Marino at the 100th percentile across every tested
radius, with a verdict of "strong support (top 5%)" — 88% letter coverage at 15 km against a
grid mean of 0%.

The number is probably correct and the inference from it is not. The comparison grid is spread
across the whole of South Australia. Most of that grid is desert, salt lake and unpopulated
scrub, where a 15 km circle contains no stations at all and therefore scores zero. A grid mean
of 0% is not telling us Marino is exceptional; it is telling us that South Australia is mostly
empty and Marino is in Adelaide.

The test that would mean something compares Marino against other **metropolitan** centres,
which is exactly what the later residential-frame work does — and under that comparison
90A Moseley Street lands 111th of 161. That is the same class of question asked with a
baseline that can actually discriminate.

Note also that the document records **I and Q uncovered at 15 km** from Marino, which is
consistent with everything since.

**Status:** retain as a record of the earlier method. Do not cite the "strong support" verdict.
The document's own closing caveat about vision-extraction error is sound and should be carried
forward.

---

## What could not be recovered

The three tool builds are not in private project storage. What is there is an earlier generation of HTML from
December 2025 — `Somerton_Man_Code_Explorer_v5.html`, `somerton v7.html`,
`Somerton_Code_Interactive_Map.html`, several Three.js flyover builds — none of which are the
current tools.

The extractor data files are in private project storage but were not included in this archive:

| File | Size |
|---|---|
| `stations.json` | 398 KB |
| `stations.csv` | 152 KB |
| `stations.db` | 180 KB |
| `wikidata_stations.json` | 45 KB |
| `needs_review.csv` | 60 KB |
| `run.log` | 13 KB |
| `sliding_window.csv` | 9.5 KB |
| `rpfa_analysis.py` | 19 KB |

Retrieve them from private project storage and place them in `data/processed/` and `src/`.
`rpfa_analysis.py` is the more valuable of the two large items: it is the only surviving script
that produces any of this, and once it is in `src/` the RPFA outputs stop being orphans.
