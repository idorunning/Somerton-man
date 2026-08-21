# Actions to Consider

Outstanding work, ordered by what it unblocks. Reviewed at the start of each session; completed
items move to `CHANGELOG.md` with a date rather than being ticked and left here.

Last reviewed: 21 August 2026.

---

## Do first

### A1. Read the Port Adelaide line off the PP47 scans
**Effort: minutes. Unblocks: open question 1, and everything downstream of the multimodal reframe.**

Open the metropolitan plates in `data/raw/maps/1938-sa-railways/` and read the
Adelaide–Port Adelaide main line directly. Is Queenstown labelled as a station between Alberton
and Portland, or is it not?

Best plates: `PXL_20250913_090404586.jpg`, `PXL_20250913_090410593.jpg`,
`PXL_20250913_090440202.jpg`, `PXL_20250913_090419827.jpg`.

Either answer is useful. If Queenstown is on the sheet, the 28 April document was right and the
Q resolution firms up. If it is not, the tramway-and-bus account stands, the multimodal reframe
is doing the work it was brought in to do, and the September 1941 service date becomes the
thing to confirm. Record the result in `CHANGELOG.md` and update
`docs/findings/prior-artefacts/README.md` either way.

### A2. Retrieve the full `rpfa_analysis.py` artefact
**Effort: two minutes. Unblocks: reproducibility of every RPFA output.**

The private project archive contains a 19 KB version. Save it to `src/`. This is the only
surviving script known to produce the imported RPFA data, and without it those outputs are
orphans by the repository's own rules.

### A3. Rerun transcription-dependent analyses
**Effort: depends on data recovery. Unblocks: confidence in the imported RPFA findings.**

The imported archive changed W to M at the start of Lines 1 and 3 and treated Line 2, rather
than Line 4, as crossed out. The standard working transcription contains seventeen distinct
letters, including W. Rerun set-membership and RPFA sensitivity checks against the standard
reading and clearly label any retained legacy outputs.

---

## Blocking the sequence test

### B1. Decide the fork
**Effort: a decision, not a task. This is the main one.**

Option A, proximity-graph approximation using existing coordinates: runnable now, cheap, and a
clean negative under generous connectivity assumptions would be a strong negative. Risks a
false positive by inventing connections and a false negative by imposing one distance threshold
on a network of wildly varying density.

Option B, build the 1948 network layer: slower, needs source work, produces a result that means
what it appears to mean.

Recommendation on the record: run A as a pilot, report it as a pilot, and treat anything other
than a clean negative as a trigger for B.

### B2. Populate the network columns
**Effort: substantial. Required for option B.**

`mode`, `route_id`, `route_seq`, `service_from`, `service_to`, `service_confirmed` — all defined
in `data/schema/locations.schema.json`, all currently empty across the whole table. With
`route_id` and `route_seq` populated, connectivity and interchange fall out for free.

Sources: Municipal Tramways Trust records, railway working timetables, municipal bus route
records.

### B3. Fix the scoring parameters before looking at any result
**Effort: an afternoon of thinking. Do it before B1, not during.**

Walkable-gap threshold, interchange penalty, time budget, and the random-string baseline all
need setting and writing into `docs/method/sequence-test-design.md` *before* the real lines are
scored. Every free parameter is a chance to tune until the hypothesis wins. Fixing them in
advance is the difference between a test and an exercise.

### B4. Decide how to treat the fourth-line strike-through
**Effort: a decision.**

The fourth line is commonly reported as crossed out. Decide whether the primary run excludes
it, includes it as an abandoned plan, or treats both readings as pre-declared variants. The
imported analysis excluded Line 2 instead; do not carry that choice forward without an
explicit variant justification.

---

## Data recovery

### C1. Pull the extractor data files from Drive
Too large to move through a chat session. Download directly and file as noted.

| File | Size | Source | Destination |
|---|---|---|---|
| `stations.json` | 398 KB | private project archive | `data/processed/` |
| `stations.csv` | 152 KB | private project archive | `data/processed/` |
| `stations.db` | 180 KB | private project archive | `data/processed/` |
| `wikidata_stations.json` | 45 KB | private project archive | `data/processed/` |
| `needs_review.csv` | 60 KB | private project archive | `data/processed/` |
| `sliding_window.csv` | 9.5 KB | private project archive | `data/processed/` |
| `run.log` | 13 KB | private project archive | `data/processed/` |

### C2. Find the three HTML tools
`rpfa-residential-frame.html`, `somerton-lab.html`, `somerton-explorer.html`. Not in Drive —
what's there is the December 2025 generation. Check local machine, Downloads, any backup. If
they're gone, `rpfa-residential-frame.html` is the only one specified well enough in
`docs/method/residential-frame.md` to rebuild faithfully; the others would be reconstruction,
not recovery.

### C3. Find the October 2025 source images
`PXL_20251014_202643575.jpg` and `Queenstowns capture.png` are cited as evidence by the
Queenstown document and exist nowhere in the project or in Drive. A document citing images
nobody can see is not evidence. If they're on the local machine, add them to `data/raw/maps/`.

### C4. Export the chat transcripts
Nineteen sessions, dates and links in `docs/sessions/README.md`. Export each from the web
interface into `docs/sessions/transcripts/` as `YYYY-MM-DD-short-title.md`. Roughly half an
hour of clicking.

### C5. Open the two untitled 3 August sessions
No titles or summaries were retained for two sessions immediately before the August export and
residential-frame work. Use the private project history to identify them, then write in what
they were without publishing private session URLs.

---

## Method hygiene

### D1. Test threshold sensitivity
Do the residential-frame rankings hold between the ≥500 and ≥1,000 population settings? If they
do, say so and the threshold stops being a worry. If they don't, the threshold is load-bearing
and needs a justification it currently doesn't have.

### D2. Account for the 1938-to-1948 decade
Every rail conclusion rests on a 1938 map used to reason about 1948 conditions. Lines opened,
closed and renamed in that decade are invisible to the source. Any station whose 1948 status
matters to a conclusion needs separate confirmation. Worth a short document listing which ones
actually matter, rather than auditing all 752.

### D3. Write producing scripts for the processed files
`extract_census.py`, `build_localities.py` — both named in `src/README.md`, neither written.
Until they exist, `data/processed/` cannot be regenerated and the repository's central rule is
aspirational.

### D4. Audit the route-designation negative
The 1948 stop-sequence search was as complete as the source data behind it, and that source
coverage has never been independently checked. A stop list with gaps could hide a match. Worth
knowing how good the coverage was before treating the negative as settled.

---

## Publication

### E1. Correct the 52 Moseley Street error wherever it survives
The 1948 electoral roll places Jessica Thomson at 90A Moseley Street. The figure 52 appears in
secondary sources and appeared in an earlier version of the blog post. Check what is currently
published.

### E2. Decide what is publishable now
The route-designation negative and the residential-frame result are both finished pieces of
work with clear verdicts. Neither depends on the sequence test. Whether to publish before the
sequence test runs is a judgement about how much of the hypothesis you want in public while it
remains unfalsified rather than supported.
