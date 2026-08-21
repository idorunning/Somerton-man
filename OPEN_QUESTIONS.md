# Open Questions

Live gaps, ordered by how much rests on them. Reviewed at the start of every working session.

---

## 1. Queenstown: what kind of place was it, and when `[LOAD-BEARING]`

Two documents in the project record flatly contradict each other, and the whole Q resolution
sits on top of the disagreement.

**Account A (28 April 2026, `docs/findings/prior-artefacts/queenstown_analysis_2026-04-28.md`):**
Queenstown was a railway station on the Adelaide–Port Adelaide main line, present on the 1938
map, roughly six stops from Adelaide central. Read at high confidence from two images.

**Account B (29 April 2026 session):** Queenstown was never an SA Railways station. It was
served by the Port Adelaide tramway — horse trams from 1882, electrified 1917, closed July
1935 — then motor bus and trolleybus from 1935 and 1938 onward.

Account B is better sourced. Account A was not reading PP No. 47 at all: its two source images
were a `PXL_20251014_*` Adelaide-environs street-and-rail map and a screen capture, neither of
which is in this repository, and it dismisses its own pipeline's flag that Queenstown is absent
from the PP47-derived canonical list. See the reconciliation note in
`docs/findings/prior-artefacts/README.md`.

Separately, the "September 1941" motor bus date recorded throughout project notes has never
been checked against a primary record, and Account B places continuous bus service from July
1935 — six years earlier.

**What rests on it:** the entire resolution of the Q problem, and therefore the justification
for the multimodal reframe. If Queenstown was not reachable by scheduled public transport in
1948, Q reverts to unresolved and Quorn at 350 km is the only candidate left.

**What would settle it:** Municipal Tramways Trust annual reports; Port Adelaide municipal bus
route records; the PP No. 47 sheet itself, read directly for a Queenstown label on the Port
Adelaide line. That last one is cheap — the scans are in `data/raw/maps/1938-sa-railways/`.

**Status:** contradicted and unresolved. Must be settled before the sequence test is run.

---

## 2. Impact of the corrected transcription `[LOAD-BEARING]`

The imported archive changed W to M at the start of Lines 1 and 3 and marked Line 2 as struck
through. The standard working transcription in the pre-existing repository uses W in those
positions and records Line 4 as commonly reported crossed out.

Correcting W restores the reported **seventeen** distinct letters: A, B, C, D, E, G, I, L, M,
N, O, P, Q, R, S, T and W. The arithmetic discrepancy is therefore resolved, but the imported
frequency and RPFA outputs were produced under the wrong line-exclusion rule.

**What rests on it:** the set-membership headline is unlikely to change because Adelaide-area
W candidates exist, but that inference is not a substitute for a reproducible rerun. RPFA
rankings may change when W is restored and the fourth-line treatment is corrected.

**Status:** transcription corrected on import; affected analyses still require rerunning.

---

## 3. The locations table has no network layer

The existing locations table is a coordinate gazetteer with map provenance. It has no
transport-mode column and no connectivity data. It is sufficient for set-membership work and
insufficient for the sequence test as designed.

**The decision to make:** either

- **(a)** a fast proximity-graph approximation using existing coordinates — treats any two
  places within a threshold distance as connected, ignores actual routes. Cheap, available
  now, and produces a weaker result that could still falsify.
- **(b)** hold for a proper 1948 network layer with mode tags and route identifiers added to
  the extraction table. Slower, requires source work, produces a result that means something.

Option (a) risks a false negative if the approximation drops real connections, and a false
positive if it invents ones. Option (b) is the test as designed.

**Status:** awaiting decision. This is the main fork in the road.

---

## 4. Orphan and missing files

Files referenced in project history that no script in `src/` currently produces, or that are
absent from the repository entirely:

| File | Nature | Action |
|---|---|---|
| `data/processed/stations.json` | 752 geocoded stations, 398 KB | Retrieve from the private project archive |
| `tools/rpfa-residential-frame.html` | Interactive lens tool | Upload local copy or rebuild |
| `tools/somerton-lab.html` | Earlier session output | Upload local copy |
| `tools/somerton-explorer.html` | Earlier session output | Upload local copy |
| Census metro municipality totals | Verified extraction | Re-run from ABS PDF, script to `src/` |
| `src/rpfa_analysis.py` | The only surviving RPFA script | Retrieve the 19 KB version from the private project archive |
| `data/raw/maps/PXL_20251014_*` | Source images cited by the Queenstown document | Not in Drive, not in the project folder. Upload if held locally. |

None of these have a producing script. Once recovered, each needs either a script in `src/`
that regenerates it, or an explicit note in `data/processed/README.md` recording that it is a
manual artefact and how it was made.

---

## 5. Census threshold sensitivity

The residential frame uses a dual threshold toggle at ≥500 and ≥1,000 persons. Neither is
principled — they were chosen as reasonable round numbers.

**Question:** does the ranking of 90A Moseley Street, and the identity of the tightest-lens
centre, change materially between thresholds? If the result is threshold-stable, say so. If it
is not, the threshold becomes a load-bearing choice and needs justifying.

**Status:** not tested.

---

## 6. Treatment of the fourth-line strike-through

Line 4 is commonly reported as crossed out. A frequency analysis may exclude it as a
correction, while a sequence analysis may retain it as an abandoned plan. Either choice is a
model decision, not a fact. The standard reading, an all-lines reading and any plausible
character variants should be pre-declared before comparison.

**Status:** open. Decide before rerunning RPFA or the sequence test, not during it.
