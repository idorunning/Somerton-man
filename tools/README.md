# Tools

Standalone single-file HTML applications. Each is self-contained and opens directly in a
browser with no build step and no server.

## Expected contents

| File | Purpose | Status |
|---|---|---|
| `rpfa-residential-frame.html` | Interactive RPFA under the residential locality frame. Draggable lens on an SVG map, centre ranking table, data / sources / method tabs. | **Missing** |
| `somerton-lab.html` | Earlier session output. | **Missing** |
| `somerton-explorer.html` | Earlier session output. | **Missing** |

All three were produced in sessions whose output directories do not persist. Drop your local
copies into this directory and they are back in the repository permanently. If the local
copies are also gone, `rpfa-residential-frame.html` can be rebuilt from
`docs/method/residential-frame.md` and `docs/findings/residential-frame-results.md`, which
between them specify the frame, the data source, the thresholds and the expected outputs.

## Convention

Tools read from `data/processed/`. They do not compute analysis that belongs in `src/` — if a
tool is the only place a number gets calculated, that number cannot be reproduced without a
browser, and it needs moving into a script.
