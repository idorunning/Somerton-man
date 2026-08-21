# Somerton Man — Itinerary Hypothesis

Original historical research into the five pencilled lines of capital letters found in the
Rubáiyát of Omar Khayyám recovered in connection with the Somerton Man case.

**The working hypothesis in one sentence:** each letter is the initial of a *place* — suburb,
town, railway station, tram stop, bus stop or locality — that Carl Webb visited or planned to
visit while searching for Jessica Thomson at 90A Moseley Street, Glenelg.

Places, not stations. Rail is one mode among several. See `HYPOTHESIS.md` before doing
anything else in this repository. `docs/hypothesis.md` preserves the broader research question,
competing explanations and the rule that transcription variants must not be silently resolved.

**Current position:** the hypothesis is unfalsified. It is not supported. Set-membership
matching cannot discriminate a genuine itinerary from a random string at the present candidate
pool size. The test that could discriminate — sequence and connectivity across a reconstructed
1948 network — has not yet been run.

---

## Repository layout

```
somerton-man/
├── README.md                  this file
├── HYPOTHESIS.md              the claim, stated precisely, with scope limits
├── ACTIONS.md                 what needs doing next, ordered by what it unblocks
├── OPEN_QUESTIONS.md          live gaps and unresolved dependencies
├── CHANGELOG.md               dated analytical decisions and pivots
├── .gitignore
├── app/                       browser-based map scaffold
├── docs/
│   ├── method/                how each analysis is constructed
│   ├── findings/              results of completed tests, negatives included
│   └── sessions/              chronological index of every working session
├── data/
│   ├── raw/                   immutable source material. never edited.
│   ├── processed/             derived data. every file regenerable from src/
│   └── schema/                column definitions and field contracts
├── src/                       scripts that turn raw into processed
├── source-manifests/          provenance manifests for retained sources
├── tests/                     automated checks and fixtures
└── tools/                     report builder and standalone HTML applications
```

## Working rules

1. **`data/raw/` is immutable.** Source scans, PDFs and transcriptions go in and are never
   modified. Corrections happen downstream, in `src/`, and are recorded in `CHANGELOG.md`.

2. **Everything in `data/processed/` must be regenerable.** If a file exists there and no
   script in `src/` produces it, it is an orphan. Orphans get flagged in `OPEN_QUESTIONS.md`
   and either reconstructed or deleted.

3. **Negative results are filed alongside positive ones.** `docs/findings/` records what
   failed as prominently as what held. The route-designation test returned a clean negative
   and it sits in the same directory as everything else.

4. **Load-bearing assumptions are labelled.** Any claim that a downstream conclusion depends
   on is marked `[LOAD-BEARING]` in the document where it appears and listed in
   `OPEN_QUESTIONS.md` until confirmed against a primary source.

5. **Every finding file opens with a date and a verdict line.** No burying the result.

## Reconstruction notes

Five artefacts are referenced in project history but are not currently in this repository,
because the environments that produced them do not persist between sessions:

| File | Status | Recovery route |
|---|---|---|
| `data/processed/stations.json` | Missing | Private project archive (398 KB, 752 geocoded stations) |
| `tools/rpfa-residential-frame.html` | Missing | Upload local copy, or rebuild from `docs/method/residential-frame.md` |
| `tools/somerton-lab.html` | Missing | Upload local copy |
| `tools/somerton-explorer.html` | Missing | Upload local copy |
| `docs/sessions/transcripts/` | Empty | Export sessions, remove private material, then add reviewed transcripts |

The 1947 Census Part VIII PDF (7.4 MB, 64 pages) is available from the ABS ausstats site and
should be placed in `data/raw/census-1947/`. Extraction via `pdftotext` with OCR-tolerant
parsing; verify numeric columns against male-plus-female sums before use.

## Source material in this repository

`data/raw/maps/1938-sa-railways/` — 20 photographs of the *Map Showing Lines of Railways in
South Australia*, June 30th 1938 (PP No. 47), signed R. H. Chapman, Chief Engineer for
Railways. Base source for all rail station verification. See the provenance note in that
directory.

`data/raw/research-reports/forensic-analysis-carl-webb/` — an unattributed three-page report
proposing a handwriting and poetic-initialism interpretation. Retained as supplied, with a
checksum and provenance note. It is not a validated forensic finding; read
`docs/findings/prior-artefacts/forensic-analysis-carl-webb-review-2026-08-21.md` before citing
it. A corrected, source-audited research note is available as an
[editable Markdown report](docs/reports/carl-webb-inscription-critical-assessment-2026-08-21.md)
and [four-page PDF](output/pdf/carl-webb-inscription-critical-assessment-2026-08-21.pdf).
