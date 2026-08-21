# Processed data

Everything in this directory must be regenerable by a script in `src/`. If a file here has no
producing script, it is an orphan: record it below and either write the script or delete the
file.

## Expected contents

| File | Produced by | Status |
|---|---|---|
| `stations.json` | manual — private archive artefact | **Missing.** Retrieve from the private project archive. 398 KB, 752 geocoded stations. No producing script exists; write one or document the manual method. |
| `census-metro-municipalities.csv` | `src/extract_census.py` (to be written) | **Missing.** Re-run extraction from the 1947 Census Part VIII PDF. |
| `localities.csv` | `src/build_localities.py` (to be written) | **Missing.** The candidate location gazetteer. Must conform to `data/schema/locations.schema.json`. |

## The gap that matters

The locations table as it stood was a coordinate gazetteer with map provenance and nothing
else. It has no transport-mode column and no connectivity data. That is enough for
set-membership work and not enough for the sequence test. See `OPEN_QUESTIONS.md` item 3.
