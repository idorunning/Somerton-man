# Finding — bounded route sequence review

Updated 5 September 2026. The previous claim of a clean negative across **all 1948 Adelaide train, tram, trolleybus, bus and coach routes** is withdrawn. No complete source network, search inputs or producing program supporting that scope was recovered.

## Reproducible result

The new standard-library program `src/review_route_sequences.py` checks four strings retained in the 21 August 2026 route and full-investigation reviews. It searches complete active lines, without gaps, in both directions and across eight M/W/C/S readings. The cancelled physical second line is kept separate.

| Prior-transcribed corridor | Initials | Complete active-line matches, all eight variants | Longest contiguous overlap, default reading |
| --- | --- | --- | --- |
| Adelaide–Marino Rocks | AMKGEEWAOHBSSMM | 0 | 2 |
| Adelaide–Henley Beach | ANBCWKWWASGGKMH | 0 | 2 |
| Adelaide–Port Adelaide | ANBCWKWWHCAP | 0 | 2 |
| Serviceton–Tailem Bend | SWBCWBKBCKTCCKYCCT | 0 | 1 |

The final overlap corrects the earlier full review's value of two. These are reused transcriptions, not a fresh complete stop-by-stop verification against 1948 operating timetables. The test neither establishes a p-value nor excludes multimodal, partial-stop or multi-day journeys.

## Route designations are a different question

No inspected source establishes that these inscription strings were official transport route designations. Earlier categorical claims about every operator's designation conventions require dated operator evidence and should not be used as a substitute for the itinerary test. A traveller's private mnemonic need not resemble an operator's route number.

## Reproduce

From the repository root:

```sh
python3 src/review_route_sequences.py
```

Inputs: `data/reference/route-sequence-inputs.json`. Output: `data/processed/route-sequence-review-2026-09-05.json`. See the [complete review](route-review-2026-09-05.md) for the stronger proposed test.
