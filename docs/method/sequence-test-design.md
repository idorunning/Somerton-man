# Sequence and connectivity test — revised design

Reviewed 5 September 2026. **The complete 1948 multimodal test has not been run.** The new four-corridor exact-string check is a separate, bounded reproduction; see [its finding](../findings/route-designation-test.md).

## Question and limits

Under a fixed vocabulary and encoding rule, do the ordered letters fit historically available journeys better than appropriate controls searched with the same flexibility?

A successful fit is conditional evidence for a model, not proof of the author, motive or exact journey. A failed fit rejects that defined model, not every possible use of travel notes. A non-significant comparison is not automatically proof of equivalence.

## Register before fitting

1. **Transcription:** physical line 2 cancelled and retained separately; eight independent W/M × W/M × C/S variants. Preserve other marks in image records.
2. **Grammar:** decide one token per place, repeated-token consistency, omissions and action tokens. Test multi-letter facility abbreviations as a separate model.
3. **Vocabulary:** freeze dated names, aliases, location types, geographic bounds and exclusions before matching.
4. **Time:** distinguish a 30 November hypothesis from another-day or multi-day hypothesis. Tickets do not date the writing.
5. **Travel:** declare permitted modes, walks, waits, operating days, accessibility and transfer rules. Include water only with independently sourced crossing evidence.
6. **Score:** fix penalties, missing-data treatment, journey budgets and all parameter sweeps. Publish the registration and input hashes.

## Network requirements

Use separate location, route and service tables. A route identifier alone does not make every pair an immediate connection. Stops need direction, order and segment travel times; services need operating dates, days and departures. Interchanges need actual access paths and allowed transfer times.

| Record | Required information |
| --- | --- |
| Location | Stable ID, dated name, type, approximate coordinates, coordinate uncertainty, source |
| Route segment | Origin/destination IDs, direction, mode, route ID, stop order, distance if sourced |
| Service | Date range, operating days, departure/arrival or explicit estimated duration, source page |
| Interchange | Connecting locations, walking or transfer rule, time and access constraints |
| Source coverage | Inspected pages, unresolved gaps, provenance and confidence |

Do not silently treat a 1938 infrastructure map as a 1948 timetable. Do not replace unavailable travel times with modern estimates without labelling a separate model.

## Search and controls

Enumerate or dynamically optimise assignments subject to the registered rules. Record complete candidates and failures, not only a winning path. Compare the best real score with the best score for each control after identical optimisation.

Use shuffled controls preserving line lengths and letter counts, alongside independent period prose and poetry initialisms. Test whether station-name sampling actually represents travel, which revisits hubs. Report the effect of glyph variants, aliases, mode changes and every tried parameter set. Calibrate significance using the full search procedure; sparse short-string frequency tables do not justify unqualified chi-square p-values.

Where practical, reserve an unused line or an independent documentary prediction before model development. The book's telephone number, ticket destinations and known case geography cannot be reused as independent confirmation after they shaped the candidate pool.

## Exploratory proximity pilot

A coordinate-threshold graph may help debug the algorithm. It is not a recovered historical network. It can invent nonexistent links and omit genuine services, so either outcome remains conditional on that approximation. A negative has stronger implications only if the approximation is demonstrably a suitable superset of real possibilities; a positive never establishes the missing historical service.

## Reproducibility gate

Publish versioned inputs, producing script, environment, seed where relevant, full outputs, source coverage and a correction log. A successful reproduction of four supplied corridor strings must never be presented as an exhaustive 1948 transport search.
