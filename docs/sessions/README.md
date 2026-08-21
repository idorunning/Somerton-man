# Session Index

Every recorded working session on this project, oldest first. This is the project's own
history: what was decided, when, and where the decision lives.

**What this file is:** a public index. Each entry carries the date and a summary of what the
session produced. Private chat URLs and account identifiers are not published here. It is not
a verbatim transcript.

**What it is not:** the full conversation record. Verbatim transcripts are not retrievable
from within a session — `/mnt/transcripts/` is empty in every environment that has been
checked. If you want full text in the repository, export each chat from the web interface and
drop the files into `docs/sessions/transcripts/` using the naming convention
`YYYY-MM-DD-short-title.md`. The index below gives the dates and titles; private project
history holds the corresponding session references.

**Review note:** these summaries preserve what each historical session did; they are not the
current authority for the inscription. The uploaded archive used M where the standard working
transcription uses W at the start of Lines 1 and 3, and treated Line 2 rather than Line 4 as
crossed out. See `../import-review-2026-08-21.md` before relying on a transcription-dependent
result below.

---

## 2025-12-13 — South Australian railway station code mapping
*Private session reference withheld from the public repository.*

First systematic letter-to-station mapping across all five code lines, worked against the 1938
map. Confirmed Quorn as the only Q-initial station, roughly 300 km from Adelaide — the opening
statement of the Q problem. Confirmed the Glenelg–Adelaide–Brighton grouping on the coastal
network, and that Marino appears on the 1938 map while Marion does not.

## 2026-02-19 — Work progress action list
*Private session reference withheld from the public repository.*

Seven-step action plan established. Systematic transcription of every visible station name
across all 20 map images, producing a structured database of 400+ stations organised by line
and region. Confirmed Marino existed in 1938 and that Marion was not established until 1954.
Delivered as a formatted Word document.

## 2026-03-07 — Reviewing Opus 4.6 improvements
*Private session reference withheld from the public repository.*

Attempted to obtain Jim Fergusson's SA railway station list (Branch Line Society SL 109) from
branchline.uk; the source was inaccessible through repeated server timeouts. Fell back to
building a 530–580 station inventory from Wikipedia, ComRails, heritage sources and the 1938
map. Re-confirmed Quorn as the sole Q-initial station across the entire network including the
Eyre Peninsula, Central Australia and Murray Mallee lines.

## 2026-04-26 — South Australian railway station database for map app
*Private session reference withheld from the public repository.*

Added a 388-entry towns and suburbs dataset alongside the station database, with 1948
transport modes tagged per entry. **This is where the hypothesis shifted from rail-only to
places-reached-by-any-mode.** Queenstown surfaced as a second Q candidate. Built a
self-contained Leaflet dashboard with dual layer toggles, transport-mode filters, draggable
centre and live letter-frequency bars.

## 2026-04-26 — Verifying 1948 coordinates against 1938 photographs
*Private session reference withheld from the public repository.*

Seven phases of database verification. Grew from 557 to 575 stations and eliminated all
low-confidence entries. Corrections included Wynarka repositioned 10 km south, Elwomple moved
to the Pinnaroo line, Wingamin corrected in spelling and line membership, 21 Eyre Peninsula
stations added, False Bay and Germein Bay removed as non-stations.

## 2026-04-26 — Somerton Man code travel itinerary analysis
*Private session reference withheld from the public repository.*

Formal briefing report under the reframed travel-itinerary model. Rebuilt RPFA using
log-likelihood ratios rather than chi-squared, with pre-registered falsification criteria.
Built `somerton-map.html`. Established the working principles that still hold: the analysis
must not be biased toward the theory, all localities are included regardless of whether their
initials match, and Line 2 is excluded from all frequency analysis.

## 2026-04-28 — Map scan inventory and processing status
*Private session reference withheld from the public repository.*

Built `sa_rail_extractor.py` through versions 0.1 to 0.3.1 — vision-API extraction,
deduplication, spell-check against a canonical list, Nominatim geocoding. Critical code review
found and fixed ten bugs. Geography restriction corrected from SA-only to Australia-wide with
SA preference, after cross-border stations (Serviceton, Cockburn, Broken Hill, Alice Springs)
were noted.

## 2026-04-29 — Queenstown Adelaide historical timeline and research gaps
*Private session reference withheld from the public repository.*

**The session that created open question 1.** Established that Queenstown was never an SA
Railways station — horse trams from 1882, electrified 1917, closed July 1935, then motor bus
and trolleybus from 1935 and 1938. Flagged that the recorded "September 1941" date could not
be verified and places continuous bus service from July 1935 onward. That discrepancy is still
unresolved.

## 2026-04-29 — Map scans app completion
*Private session reference withheld from the public repository.*

Built `rpfa-map.html` (~178 KB) — Leaflet, CartoDB Voyager tiles, all 752 real stations
embedded, confidence-based markers, 26-letter filter grid, radial RPFA with draggable centre
and χ² scoring. Notable for a correction: an earlier build used a fabricated starter dataset
and was rejected outright. No invented data.

## 2026-05-01 — Rewriting the Somerton Man code blog post
*Private session reference withheld from the public repository.*

WordPress-ready rewrite built around the multimodal reframe and the Q resolution. Developed
the GAB ending of Line 5 and the reading of Line 2 as an abandoned plan. Flagged a factual
error carried from the original post: Jessica Thomson's address is 90A Moseley Street on the
1948 electoral roll, not 52. Also produced the full case chronology from April 1947 to the
2022 identification.

## 2026-05-21 — Reworking routes with accurate town locations
*Private session reference withheld from the public repository.*

Route reconstructions tested against the documented timeline. Identified them as consistent
with the 19-month void rather than a single-day itinerary, and flagged the absence of an H for
Henley Beach and the unresolved eight-hour gap. Produced a Word report, an EPUB validated to
3.2 against epubcheck, and a WordPress HTML bundle. **This is the session where the standing
instruction against the word "honest" was set.**

## 2026-06-01 — Consolidated timeline
*Private session reference withheld from the public repository.*

Audit of map sources across the project folder and Drive. Confirmed 20 images in the project
folder and only two in Drive `Map scans/Map 1/`, with no duplicates and no `map_scans`
subfolder anywhere. Established that the station database was compiled by cross-referencing
external sources against the maps, not by exhaustive transcription of every visible label.

## 2026-06-01 — Somerton Man travel itinerary code hypothesis review
*Private session reference withheld from the public repository.*

Consolidated assessment document. **The falsifiability problem was confirmed empirically
here:** every distinct letter already has an Adelaide-reachable candidate in the extracted
subset, so set-membership cannot discriminate. Also established that the locations table is a
coordinate gazetteer with no transport-mode column and no connectivity data — open question 3,
and it has not moved since.

## 2026-06-12 — Somerton Man identity: Jessica Thomson connection theory
*Private session reference withheld from the public repository.*

Built `somerton-explorer.html` then redesigned it as `somerton-lab.html` — four tabs, RPFA
lens with a find-tightest-lens optimiser, route tracer, full source registry of all 20 scans
with plate citations, drag-and-drop image attachment with IndexedDB persistence. The RPFA
result of that build: tightest lens ≈7.06–7.10 km near Rosewater/Wingfield, binding
constraints at Q, I and L.

## 2026-08-03 — *(untitled, no summary recorded)*
*Private session reference withheld from the public repository.*

No title or summary was retained. Content unknown. Worth opening and recording what it was.

## 2026-08-03 — *(untitled, no summary recorded)*
*Private session reference withheld from the public repository.*

No title or summary was retained. Content unknown. Worth opening and recording what it was.

## 2026-08-05 — Full project export
*Private session reference withheld from the public repository.*

33-file, 2.8 MB archive: all 20 scans, a markdown dossier, structured CSVs, and a completed
source registry mapping every scan to its plate — including identification of the three key
working plates and the two plates corroborating Quorn. First session where the absence of
`stations.json`, `somerton-lab.html` and `somerton-explorer.html` was formally documented.

## 2026-08-06 — Mapping likely destinations using RPFA
*Private session reference withheld from the public repository.*

Two pivots. The residential locality reframe using 1947 census data with the dual threshold
toggle, and the transport route designation test, which returned a clean negative. Built
`rpfa-residential-frame.html`. Headline: 14.39 km from Moseley Street, Islington binding,
111th of 161; tightest lens anywhere 5.40 km near West Croydon. Metropolitan municipality
totals reconciled exactly to 382,454 persons.

## 2026-08-21 — Setting up a GitHub repo for chat storage
*Private session reference withheld from the public repository.*

Scoping conversation. Established that pushing to GitHub directly is not possible from a
session and that the deliverable is a ready-to-commit bundle instead.

## 2026-08-21 — Repository consolidation
*(this session)*

Repository built and committed. Hypothesis restated as places of any kind rather than railway
stations. Two discrepancies logged: the seventeen-versus-sixteen distinct-letter count, and
the four artefacts with no producing script. The letter-count discrepancy was traced to the
archive transcription error and corrected during the GitHub import later that day.
