# Data provenance

## Provenance standard

Every dataset or extracted record must identify:

- source title and holding institution;
- creator or publisher;
- source date and edition;
- stable URL, catalogue reference or archive reference;
- page, sheet or map location;
- access date;
- extraction method;
- person or script responsible;
- transformations applied;
- known limitations;
- licence or reuse status where known.

## Dataset register

| Dataset | Source | Raw/derived | Extraction method | Last checked | Limitations |
|---|---|---|---|---|---|
| `data/stations.csv` |  | derived |  |  | Initial scaffold |

## Retained source artefacts

| Artefact | Source | Received | Integrity | Limitations |
|---|---|---|---|---|
| `data/raw/research-reports/forensic-analysis-carl-webb/Somerton_Man_Forensic_Analysis_Carl_Webb.pdf` | supplied by repository owner through a project upload | 2026-08-21 | SHA-256 recorded in `source-manifests/research-reports.csv` | author, date, qualifications, issuing body and rights status not stated; not a validated forensic report |

## File integrity

Where source files can lawfully be retained, record a SHA-256 checksum in the relevant manifest. Do not overwrite raw source material; create a new version and document the change.
