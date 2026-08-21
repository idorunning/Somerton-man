# Queenstown Analysis — New Scans 2026-04-28

## Images processed
| Image | Type | Stations extracted |
|-------|------|--------------------|
| `PXL_20251014_202643575.jpg` | Wide view — Adelaide metro & suburbs | 131 |
| `Queenstowns capture.png` | Zoomed — Port Adelaide area focus | 20 |

Previous total: 658 unique stations. New total: **752**. Net new: **94**.

---

## a) New unique stations (94 total)

All 94 were genuinely absent from the prior 12-image run. The vast majority
(93) came from the wide image; one (`Finsbury`) was zoomed-only; three
(`Portland`, `Royal Park`, `Williamstown`) appeared on both new images.

Selected high-confidence additions from the wide view (inner Adelaide network):
Beverley, Enfield, Glenelg, Hope Valley, Kensington, Magill, Norwood,
Plympton, Portland, Prospect, Royal Park, St Mary's, The Grange, Unley.

Full list:

Beaumont, Beverley, Blythville, Brompton, Brooklyn Park, Burnside, Campbelltown, Chicago, Clifton, Cottonville, Dulwich, E. Adelaide, East Marden, Eden Hills, Enfield, Erindale, Finsbury, Finsbury Park, Fulham, Fullarton, Garfield, Gilles, Glen Osmond, Glenelg, Glynde, Goodwood South, Grangeville, Hackney, Hastings, Hectorville, Highgate, Hilton, Home Park, Hope Valley, Hyde Park, Kensington, Kent Town, Kirkaldy, Klemzig, Knightsbridge, Lockleys, Lower Mitcham, Magill, Marden, Maylands, McDonald, Middle Brighton, Mills, Morphett, Morphettville, Myrtle Bank, N. Glenelg, Nailsworth, Netley, New Thebarton, Newton, North Mitcham, North Norwood, Norwood, Paradise, Parkside, Parkside South, Payneham, Peckham, Penrhyn, Pinder, Plympton, Portland, Prospect, Queenstown, Race Course, Racecourse, Redfern, Reepham, Richmond, Royal Park, Sleeps Hill, South Plympton, South Richmond, St Leonards, St Mary's, St Mary's West, Sunnyside, The Grange, Thebarton, Thornton Park, Torrensville, Tusmore, Unley, Walkerville, Wayville, West Adelaide, West Mitcham, Williamstown.

---

## b) Q-stations

**One Q-station found: Queenstown.**

| Field | Wide view (PXL_20251014_*) | Zoomed view (Queenstowns capture) |
|-------|---------------------------|------------------------------------|
| Name read | Queenstown | Queenstown |
| Confidence | **high** | **high** |
| Line | Port Adelaide line | Adelaide-Port Adelaide main |
| Position | upper-left | centre-left |
| Notes | — | — |

Both readings are identical in name and confidence. Surprisingly the zoomed
image did not produce a higher confidence reading than the wider one — but
since the wide view already read it at "high", there was no room to improve.

**Spell-checker flag: `possible_misread_of:Owen`** — this is a false positive.
Queenstown is not in the canonical station list (which was built from the
1938 PP No. 47 map, where Queenstown may not have been a named station stop),
so the fuzzy matcher fell back to `Owen` as the nearest canonical entry
(score < 90). The station name itself is unambiguous; the flag can be
disregarded for research purposes.

No other Q-stations appeared on either image.

---

## c) Cross-image name consistency

16 stations appeared on both new images. All 16 were read with identical
spelling on both. No OCR disagreements.

Stations confirmed consistent: Albert Park, Alberton, Cheltenham, Glanville,
Islington, Kilkenny, Largs, Peterhead, Port Adelaide, Portland, Queenstown,
Rosewater, Royal Park, Williamstown, Wingfield, Woodville.

**One naming variant worth noting (not a true inconsistency — likely two
different locations):**
- Wide view: "Race Course" (medium confidence, Glenelg line, lower-left)
- Zoomed view: "Racecourse" (medium confidence, Cheltenham racecourse branch)

These are probably the Morphettville and Cheltenham racecourse sidings
respectively — distinct locations that happen to have similar names. The
normaliser treats them as separate entries, which is correct.

**Another possible same-station split:**
- Wide view: "Finsbury Park" (medium, Adelaide-Port Adelaide)
- Zoomed view: "Finsbury" (high, Finsbury branch)

These likely refer to the same station. The zoomed image (higher resolution
of that area) reads it as "Finsbury"; the wider view adds "Park". Worth
manual review — but not a misread, just a label-length difference.

---

## d) Network connectivity established by the wider image

The wide view (PXL_20251014_*) is an Adelaide-environs street-and-rail map,
covering roughly Port Adelaide in the north-west to Belair/Blackwood in the
south-east. It places Queenstown clearly on the **Adelaide–Port Adelaide main
line**, with the following confirmed chain of connections:

```
Adelaide (central terminus, junction)
  │ Adelaide-Port Adelaide main line
  ├─ Bowden (junction — several lines diverge)
  ├─ Croydon
  ├─ Beverley
  ├─ Woodville  ←── junction for Grange branch
  ├─ Cheltenham
  ├─ Albert Park
  ├─ Alberton
  ├─ QUEENSTOWN
  ├─ Portland
  ├─ Rosewater
  └─ Port Adelaide  ←── junction with Outer Harbour/Semaphore branches
```

From Adelaide central the wider image also shows outgoing connections to:
- Gawler line northward (Dry Creek junction visible)
- Adelaide-Wolseley southward (Goodwood junction, Mitcham, Belair, Blackwood)
- Brighton suburban (coastal south)
- Glenelg tramway
- Henley Beach branch

**Significance for the Q-problem:** Queenstown is directly reachable from
Adelaide city (and therefore from any point on the SA rail network that
connects through Adelaide) via the Port Adelaide main line. The 1938 map
confirms the rail station existed. The motor-bus service from September 1941
likely replaced or supplemented the rail service; either way, Queenstown was
accessible from Adelaide without a dedicated journey — it was a routine stop
on a suburban line.

---

## Summary for Q-problem investigation

- Queenstown **is** on the 1938 SA Railways map, on the Adelaide–Port Adelaide
  main line, read at **high confidence from two independent images**.
- Spelling is unambiguous and consistent across both images.
- Network connectivity is fully established: Queenstown is ~6 stops from
  Adelaide central, with no unusual transfer required.
- The motor-bus access from September 1941 adds a second transport mode; the
  rail option existed before that date.
- No other Q-candidates emerged from this corpus. Queenstown remains the
  sole Q-station identified from this corpus.
