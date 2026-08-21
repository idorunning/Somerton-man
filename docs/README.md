# Documentation

`method/` — how each analysis is built. Written so that someone with the raw data and no
memory of the project could reconstruct the work. Records the choices made, and which of those
choices are unprincipled.

`findings/` — results. One file per completed test. Every file opens with a date and a verdict
line. Negatives are filed here on the same footing as positives; the route-designation test
returned a clean negative and it belongs in the record exactly as prominently as anything that
held.

`sessions/` — dated summaries of historical working sessions. Private session URLs are not
published. The summaries record what was done at the time and are not authoritative where a
later correction exists.

`import-review-2026-08-21.md` — review of the uploaded repository snapshot, including the
transcription correction, privacy redactions and the reproducibility limits of the imported
findings.

`findings/prior-artefacts/forensic-analysis-carl-webb-review-2026-08-21.md` — claim and methods
audit of the unattributed handwriting-analysis PDF retained under `data/raw/research-reports/`.
The report is hypothesis-generating material, not a current forensic finding.

`reports/carl-webb-inscription-critical-assessment-2026-08-21.md` — corrected, source-audited
assessment of the report's technical-lettering and initialism hypotheses. The editable
Markdown is authoritative; a reader-formatted PDF is at
`../output/pdf/carl-webb-inscription-critical-assessment-2026-08-21.pdf`.
Regenerate it with `python tools/build_carl_webb_report.py`; this requires ReportLab and the
DejaVu font family.

## Filing a new finding

Copy the pattern:

```markdown
# Finding — [short name]

**Date:** YYYY-MM-DD
**Verdict: [one or two sentences. Lead with the result, not the setup.]**

## What was tested
## Result
## What this does and does not mean
## Caveats
```

Do not write a finding without a caveats section. If there genuinely are none, say so
explicitly rather than omitting the heading.
