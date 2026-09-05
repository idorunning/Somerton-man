# Somerton Man — Itinerary Hypothesis

Original historical research into the five pencilled lines of capital letters found in the
Rubáiyát of Omar Khayyám recovered in connection with the Somerton Man case.

**Working hypothesis:** the inscription may encode an itinerary using place-name initials, across one or more transport modes. Its author, writing date, actual journey and purpose are not established. A proposed search for Jessica Thomson is an additional inference, not the foundation of the model.

**Reviewed 5 September 2026:** read the [complete sourced review](docs/findings/route-review-2026-09-05.md), [revised hypothesis](HYPOTHESIS.md) and [interactive route section](app/route-review.html).

The review corrects the cancelled-line treatment, map provenance and unsupported claims of an exhaustive 1948 transport test. A new reproducible four-corridor check covers eight readings and finds no complete active-line matches. The broader multimodal theory remains unproven; no complete dated network was recovered. Legacy frequency and geographic-centre outputs remain not reproduced.

The new section is additive and ready for integration. The separate deployed 24-page Netlify archive has not been refreshed: its source download was blocked by browser URL policy. See [integration notes](app/INTEGRATION.md).

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
├── app/                       interactive review and original map scaffold
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
└── tools/                     standalone HTML applications
```

## Working rules

1. **`data/raw/` is immutable.** Source scans, PDFs and transcriptions go in and are never
   modified. Corrections happen downstream, in `src/`, and are recorded in `CHANGELOG.md`.

2. **Everything in `data/processed/` must be regenerable.** If a file exists there and no
   script in `src/` produces it, it is an orphan. Orphans get flagged in `OPEN_QUESTIONS.md`
   and either reconstructed or deleted.

3. **Negative results are filed alongside positive ones.** `docs/findings/` records what
   failed as prominently as what held. The bounded route-string result states its exact
   scope and does not claim an exhaustive 1948 network search.

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

