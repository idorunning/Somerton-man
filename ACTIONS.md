# Next research actions

Reviewed 5 September 2026. The [full review](docs/findings/route-review-2026-09-05.md) explains these priorities. Completed corrections are in `CHANGELOG.md`.

## 1. Freeze the transcription and model

- Obtain two independent readings of the published reproduction and, if available, a better authenticated image. Preserve glyph uncertainty and separate graphic marks.
- Treat physical line 2, `MLIAOI`, as cancelled in the primary reading; retain it as a separate sensitivity observation. The previous long-line cancellation claim is corrected.
- Predeclare M/W alternatives at physical lines 1 and 3 and C/S at line 4's end. The eight-variant bounded rail test is now reproducible.
- Define geography, date window, repeated-letter consistency, omissions, allowable modes, walking and multi-letter tokens before any larger search. AQS as one facility is a separate grammar.

## 2. Build a dated 1948 transport layer

Prioritise MTT timetables and fare stages, the St Leonard's running journal, SAR working timetables and service notices, contemporary directories and Port Adelaide bus records. Record each source at page or item level.

Queenstown is visibly a locality on the undated environs image and is not a stopping-place label on the inspected 1938 SAR inset. The old Albert Park tram line closed in November 1934; the remaining Port Adelaide lines closed in July 1935. Verify a 1948 connection rather than carrying forward an unspecified bus replacement date.

For Torrens Island quarantine, confirm the landing point, water service, access restrictions and reason for a visit. NAA catalogued visitor, hospital and nurse records cover 1948, but the entries have not been read. The 1887 phrase Adelaide Quarantine Station does not establish the acronym AQS in 1948.

Use a separately dated source for changes between the 1938 map and 1948. A 1971 map can be contextual only. The April 1949 tourist map and 1947 tour material catalogued in the Peter Spearritt collection are promising near-period leads, not inspected 1948 operating records.

## 3. Recover exact analysis inputs

The full RPFA script, candidate gazetteer, population thresholds and producing configurations are still needed. Legacy values 14.39 km, 111/161 and 5.40 km must remain labelled not reproduced.

Previously referenced artefacts include `stations.json`, `stations.csv`, `stations.db`, `wikidata_stations.json`, `needs_review.csv`, `sliding_window.csv`, `run.log`, the full `rpfa_analysis.py`, and the residential-frame and laboratory HTML tools. A recovered file needs provenance and a producing script before its output is reused. Placeholder repository data do not establish that these original datasets were recovered.

## 4. Run a fair sequence comparison

Freeze scoring, time budgets, transfer penalties and all search freedoms. Fit the same algorithm to the real inscription, shuffled controls preserving counts and line lengths, and period prose/poetry initials. Optimise every control identically and account for every tested variant.

A proximity-only graph may be a labelled exploratory pilot. Its negative result cannot falsify the dated network unless it is shown to include all relevant real connections and comparable costs; its positive result cannot establish that an actual service existed.

## 5. Seek independent documentary evidence

Follow the public X3239 advertisement trail, household occupancy, possible appointments and independently sourced handwriting. Do not infer a particular motive, authorship or cause of death from letter fitting. Access failures are not negative name searches.

## 6. Complete the website integration

The additive redesigned section is `app/route-review.html`. The current Netlify archive has separate source and 24 pages; it must be updated from its own source checkout. Its source download was blocked by browser URL policy in this session. Obtain the existing source ZIP, integrate this section and preserve its pages and access settings, then build and deploy. No live refresh is claimed by this research commit.

Original Drive map bytes also remain inaccessible. The 20 repository derivatives and the published inscription reproduction have been inspected; higher-resolution originals may improve reading confidence.
