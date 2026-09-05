# Route review integration

Prepared 5 September 2026. `route-review.html` is a complete static review section with companion CSS, JavaScript and two added image assets. Its SAR scan points to the unchanged repository JPEG. No build step is needed for this static section.

## Included

- Full sourced research review, corresponding to `docs/findings/route-review-2026-09-05.md`.
- Modern geographic locator with documented/candidate filters and source-specific detail cards. All marker positions are approximate; no historic route polyline or calculated travel time is implied.
- Separate source-image viewer with zoom, rotation and fit-width controls. The original retrieved bytes remain unchanged.
- Eight-combination transcription explorer and bounded route-test findings, produced by `src/review_route_sequences.py`.
- Responsive layout, keyboard controls, textual evidence labels, reduced-motion support and printable review text.

The geographic map loads Leaflet 1.9.4 and OpenStreetMap tiles online, with attribution. Evidence cards, transcription and embedded report work without those services. A portable reading copy can embed the local CSS/JS/images; it still needs internet access for map tiles and external source links.

## Existing website

The current archive is `wrgoababd-review.netlify.app`, separate from this research repository. Its inspected deployment contains 24 generated pages. The browser URL policy blocked its source download in this session. This addition is not a replacement for that site's source and has not been deployed.

Integrate into the existing application once its source ZIP or checkout is available. Preserve its routes, documents, authentication/access settings and unrelated content. Copy the added asset files and existing SAR frame into appropriate public paths, scope CSS to avoid clashes, and adapt links/navigation to the existing framework. Do not deploy this repository root over the existing archive.

## Evidence assets

| Asset | Provenance and boundary |
| --- | --- |
| `assets/adelaide-environs.jpeg` | Unchanged 900 × 1106 raster extracted from the earlier project map; publication date and catalogue identity unverified |
| `assets/somerton-code.jpg` | Unchanged 1802 × 1440 police reproduction downloaded from Wikimedia Commons; [source and public-domain statement](https://commons.wikimedia.org/wiki/File:SomertonManCode.jpg); downloaded and viewed 5 September 2026, not the original book |
| `../data/raw/maps/1938-sa-railways/PXL_20250913_090410593.jpg` | Existing small repository derivative, displayed with rotation only; SAR metropolitan enlargement, 1938 report context |

## Verification and remaining work

The producing rail test includes an independent exhaustive-substring validation; results are checked for all eight readings and both directions. JavaScript syntax and HTML structure, IDs, internal links and asset presence are checked without a browser. Static evidence/accessibility review corrected source-copy wording, screen-reader announcements and fit-width labelling.

No browser interaction, visual layout or live deployment test is claimed. After integration into the actual website, its normal build and deployment gates still need to run; confirm the live deployment before marking the refresh complete.
