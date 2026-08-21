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
