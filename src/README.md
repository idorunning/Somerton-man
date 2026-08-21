# Scripts

One script per derived artefact. Each script:

- reads only from `data/raw/`
- writes only to `data/processed/`
- is runnable from the repository root with no arguments
- states its inputs and outputs in a docstring at the top

## To be written

| Script | Purpose |
|---|---|
| `extract_census.py` | Parse metropolitan municipality totals from the 1947 Census Part VIII PDF. OCR-tolerant numeric parsing; verify every row against its male-plus-female column sum before emitting. |
| `build_localities.py` | Assemble the candidate location gazetteer conforming to `data/schema/locations.schema.json`. |
| `rpfa.py` | Radial Proximity Frequency Analysis. See `docs/method/rpfa.md`. |
| `sequence_test.py` | The sequence-and-connectivity test. Blocked. See `docs/method/sequence-test-design.md`. |

## Known extraction notes

`pdftotext` is the reliable route into the 1947 Census PDF (7.4 MB, 64 pages). Column
alignment survives it; layout-mode output is worth trying first. Numeric columns are the
OCR-fragile part — always reconcile against the sex-split subtotals rather than trusting a
single parsed figure.
