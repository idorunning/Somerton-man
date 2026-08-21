# Import review — 21 August 2026

## Scope

This review covers the uploaded `somerton-man-repo.zip` before its contents were integrated
with the existing public GitHub repository. The archive contained a clean, four-commit Git
repository with 43 tracked files. Its embedded `.git/` directory was not imported; the files
were added as a reviewed snapshot on top of the existing repository history.

The existing map scaffold, extraction scripts, research-question documents, data stubs, tests
and source manifest were preserved.

## Material correction

The archive's top-level transcription used M at the start of Lines 1 and 3 and marked Line 2
as struck through. The pre-existing repository records the standard working transcription as:

```text
WRGOABABD
MLIAOI
WTBIMPANETP
MLIABOAIAQC
ITTMTSAMSTGAB
```

The fourth line is commonly reported as crossed out. Restoring W resolves the apparent
sixteen-versus-seventeen distinct-letter discrepancy.

This is not only a typographical correction. Historical RPFA work described in the archive
excluded Line 2 and may therefore have used the wrong analysis set. Those outputs are retained
as historical results but require a reproducible sensitivity rerun using a frozen, documented
transcription variant. The correction and its consequences are recorded in `CHANGELOG.md`,
`ACTIONS.md` and `OPEN_QUESTIONS.md`.

## Public-repository hygiene

The archive contained a personal email address, private cloud-storage identifiers and direct
links to private chat sessions. They were removed from the public import. Dates, titles,
summaries, filenames and recovery requirements were retained where they remain useful.

The twenty JPEG map photographs contain valid JPEG data and no exposed camera or GPS metadata
was detected in the imported files. The JSON Schema in `data/schema/locations.schema.json`
parses successfully.

## Evidential status

The archive usefully consolidates the working hypothesis, negative findings, method design,
source photographs, session chronology and outstanding work. It does not supply the missing
processed datasets or producing scripts needed to reproduce the numerical RPFA results.

Accordingly:

- the route-designation result remains a recorded negative whose source coverage needs audit;
- the residential-frame figures remain historical results pending data and script recovery;
- the set-membership conclusion is plausible but should be rerun after the transcription
  correction; and
- the sequence-and-connectivity test remains unrun and is still the principal discriminating
  test for the itinerary hypothesis.
