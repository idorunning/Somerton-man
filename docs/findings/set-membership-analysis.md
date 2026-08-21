# Finding — Set-membership analysis

**Date:** prior session, undated
**Verdict: coverage cannot discriminate. Every distinct letter in the code has at least one
Adelaide-reachable candidate place, so a random string drawn from the same alphabet would be
equally coverable. Set-membership analysis is exhausted as a test.**

## What was tested

Whether every letter appearing in the five code lines can be matched to at least one place
within reach of Adelaide, using the multimodal candidate pool.

## Result

Yes. Every one. No letter fails.

## Why this is not good news

A hypothesis that cannot fail a test learns nothing from passing it. If the code lines had
contained a letter with no possible Adelaide-area candidate — a Z, an X — that would have been
a genuine falsification opportunity, and surviving it would have counted for something. They
do not, and it did not.

The letter distribution in the code is unremarkable. It draws on common initials in a place-name
alphabet where common initials are exactly what an Australian suburban gazetteer is full of.

## Consequence

This is what forced the sequence test to the top of the queue. It is not an optional refinement
of the set-membership work; it is the replacement for it. Coverage was the last question the
gazetteer alone could answer, and it has been answered unhelpfully.

## Transcription review

The imported archive had changed W to M at the start of Lines 1 and 3, producing a false count
of sixteen distinct letters. The corrected standard transcription contains seventeen. Known
Adelaide-area W candidates mean the headline coverage conclusion is not expected to change,
but the test should still be rerun from versioned inputs before this finding is treated as
fully reproduced. See `OPEN_QUESTIONS.md` item 2.
