# Changelog

## 5 September 2026 — itinerary, source-map and reproducibility review

- Corrected the cancelled-line attribution: the short physical second line is the primary cancelled reading. Retained M/W and C/S sensitivity variants and withdrew the claim that excluding line 2 was an inherent error.
- Reproduced four prior-transcribed corridor strings under all eight variants and both directions: 256 active comparisons, no full-line matches. Corrected the Serviceton–Tailem Bend maximum overlap from two to one. Withdrew the unsupported all-1948-network negative.
- Relabelled historical frequency and radius results as not reproduced; separated fixed-pool coverage from a sequence test and removed the unsupported natural-centre interpretation.
- Audited 20 repository derivatives and 19 Drive metadata entries. Corrected regional frame labels, national-map provenance, original-file claims and map-date limitations. Existing raw JPEG checksums are unchanged.
- Confirmed Queenstown as a locality on the undated environs raster, without establishing a railway stop or 1948 service. Recorded historic Adelaide Quarantine Station wording and the necessary water-access question as research leads.
- Added a sourced full review, corrected methods and priorities, and a responsive route-review page with modern locator, source-image viewer, transcription controls and explicit uncertainty.
- Live integration remains pending the separate existing Netlify source. Browser URL policy blocked its source download; the 24-page archive and access controls were not replaced.


Analytical decisions and pivots, newest first. This is a record of *why* the analysis changed,
not a list of file edits.

Entries recovered from project history before this repository existed are marked as such and
carry no date, because the dates were not preserved. Everything from 2026-08-21 onward is
dated at the point of decision.

---

## 2026-08-21 — Transcription corrected during GitHub import

The uploaded archive transcribed the initial character of Lines 1 and 3 as M and treated Line
2 as struck through. The pre-existing repository's standard working transcription uses W in
those two positions and records Line 4 as commonly reported crossed out.

The top-level hypothesis and method documents were corrected during import. Restoring W
resolves the seventeen-versus-sixteen count discrepancy. Historical RPFA outputs that excluded
Line 2 remain evidence of what was previously run, not validated results under the corrected
transcription. Rerunning the affected analyses is now an explicit action and open question.

## 2026-08-21 — Repository established

Project consolidated into a structured repository. Working rules adopted: raw data immutable,
processed data regenerable, negatives filed alongside positives, load-bearing assumptions
labelled.

Two things were flagged on consolidation:

- The distinct-letter count in the falsifiability finding is recorded as seventeen in project
  notes but counts as sixteen against the transcription in `HYPOTHESIS.md`. Logged as open
  question 2. This was traced to a transcription error and resolved during GitHub import later
  the same day; the affected analyses still require rerunning.
- Four artefacts referenced in project history have no producing script and are absent from
  the repository. Logged as open question 4.

The hypothesis statement was rewritten to make the scope explicit at the top of the
repository: each letter is the initial of a *place* of any kind reachable from Adelaide, not a
railway station. The rail-only reading had already been abandoned analytically but was still
implicit in how the material was organised.

---

## Prior session — Route designation test *(undated)*

Tested whether the code lines correspond to transport route designations rather than place
initials. Clean negative.

Municipal Tramways Trust trams used numeral route numbers from 1917. Buses and trolleybuses
used destination names only. Letter-suffix route codes did not exist in Adelaide until 1962.
No exact consecutive stop-initial match was found for any of the five code lines on any 1948
Adelaide train, tram, trolleybus, bus or coach route, in either direction.

Filed at `docs/findings/route-designation-test.md`.

---

## Prior session — Residential locality reframe *(undated)*

Candidate pool reframed from transport stops to residential localities, using 1947
Commonwealth Census population data with a dual threshold toggle at ≥500 and ≥1,000 persons
rather than a fixed cut-off.

Metropolitan municipality totals extracted from the 1947 Census Volume I Part VIII PDF via
OCR-tolerant parsing and reconciled exactly against male-plus-female column sums.

Headline results: 90A Moseley Street requires a 14.39 km radius to cover all code letters,
with Islington as the binding constraint, ranking it 111th of 161 candidate centres. The
tightest possible lens anywhere is 5.40 km, centred near West Croydon in the inner north-west.

This produced a materially different picture from the transport-stop frame and placed the
Moseley Street anchor in the bottom third of candidate centres. Recorded as a quantitative
result that contextualises the hypothesis rather than confirming or falsifying it.

Filed at `docs/findings/residential-frame-results.md`.

---

## Prior session — Set-membership analysis *(undated)*

Established that every distinct letter in the standard transcription already has at least one
Adelaide-reachable candidate place. Coverage therefore cannot discriminate the code from a
random string drawn from the same alphabet.

Consequence: set-membership analysis is exhausted as a discriminating test. The
sequence-and-connectivity test becomes the necessary next step rather than an optional
refinement.

Filed at `docs/findings/set-membership-analysis.md`.

---

## Prior session — Multimodal reframe *(undated)*

Framework expanded from South Australian Commissioner's Railways only to a multimodal pool
covering rail, the Glenelg tram, and municipal motor bus routes.

Driver: the Q problem. Quorn is the only Q-initial station on the South Australian railway
network and sits roughly 350 km from Adelaide. A rail-only frame leaves Q permanently
unresolved. Queenstown, an inner suburb served by motor bus, resolves it — conditional on the
service date, which remains unconfirmed.

---

## Origin — Rail-only framework *(undated, superseded)*

Initial framework treated the candidate pool as South Australian railway stations. Superseded
by the multimodal reframe and then by the residential locality reframe. Retained here for the
record.

