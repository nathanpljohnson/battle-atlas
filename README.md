# Battle Atlas

This is a library of Osprey-style 3D battle maps, one page with a tab for each battle. Each battle is shown on real terrain, with unit blocks (infantry, cavalry, artillery, light troops), movement arrows, numbered events, narrative and tactics notes, confidence levels and sources, stepped through a timeline.

- **Published library:** https://battle-atlas.johnna1203600.chatgpt.site (ten battles, including Leuthen; Site version 18). The older Claude artifact is https://claude.ai/artifact/Gbh8cmwciTY9jRqqHbMX54 and was not updated in this release.
- **Add a battle:** run `/battle-map <battle name and year>` in Claude Code. The full research and verification method is in `~/.claude/commands/battle-map.md`.

## Layout
```
library.json              ordered list of battle ids shown in the library
engine/index.src.html     the renderer (three.js 0.147 + OrbitControls, from CDNs); placeholders /*MANIFEST*/[] and /*INLINE*/null
tools/terrain.py          python3 tools/terrain.py battles/<id>    -> terrain.json (+ terrain_raw/filled.png previews)
tools/battlekit.py        authoring kit used by each scenario.py; validates and exports <id>.json + check.png
tools/build_library.py    python3 tools/build_library.py           -> dist/index.html, dist/battles/*.json, dist/preview.html, dist/battle-atlas-offline.html
battles/<id>/             sources/, brief.md, places.json, terrain_config.json, terrain.json, scenario.py, <id>.json, check.png
battles/rossbach/make.py  converts the original Rossbach project (../rossbach/) into the library format
dist/                     the built site: publish index.html with battles/*.json as files; preview.html runs straight from disk
```

## Adding a battle by hand
1. **Folder.** Create `battles/<id>/` and add `places.json` (`{name: [lat, lon]}`) and `terrain_config.json` (`{"bbox": [W, S, E, N], "masks": [], "bumps": []}`).
2. **Terrain.** Run `python3 tools/terrain.py battles/<id>`, then look at the PNGs and add masks or bumps for modern changes to the ground.
3. **Scenario.** Copy `battles/austerlitz/scenario.py` as `battles/<id>/scenario.py` and rewrite it.
4. **Build.** Run `cd battles/<id> && python3 scenario.py`, which writes `<id>.json` and `check.png`. Compare `check.png` with the source maps.
5. **Add it.** Add the id to `library.json`, then run `python3 tools/build_library.py`.

## Data contract (`<id>.json`)
- `meta`:
  - `title`, `year`, `eyebrow`, `subtitle`
  - `sides {key: {name, top, side, mark, arrow, flag}}` (colours)
  - `belligerents [{name, commander, sides[], code: letters|numbers}]`
  - `forces {start, end: [{label, n, segs: [[side, fraction]]}]}`
  - `sun {lat, decl, note}`, `view {az, el}`, `unitScale`, `unitLabelDist`, `ground {season: autumn|winter, relief}`
  - `method`, `sources [{label, url, note}]`, `notes`
- `terrain`: `{w, h, bbox, exag, b64}`, where `b64` holds uint16 little-endian values of (elevation − min) × 10, rows north first.
- `phases []`: `{t, label, title, text, tactic: [heading, body], arrows: [{s, k: move|charge|retreat|fire, p: [[lat, lon], ...]}], events: [[lat, lon, text]], focus: [lat, lon, dist_km], conf?, debate?}`
- `units []`: `{id, side, type: inf|gd|cav|lc|art|lt, name, strength, w (frontage m), keys: {phase: [lat, lon, facing°, form X|C|L|F|R, bend?]} (bend bows the line: + convex toward facing, - concave; moves keep formation unless a C key or a ride over 2.5 km makes them snake), note, conf?, lines?, blocks?, code?}`
  - Keys carry forward: a phase with no entry keeps the previous one.
  - The number of blocks is read from `strength`: "N bns", "N sqns" or "N guns".
- `hq []`: `{id, side, name, keys: {phase: [lat, lon]}, note}`
- Scenery:
  - `places {name: [lat, lon, size?]}`, `hills {name: [lat, lon]}`
  - `roads [[name or [lat, lon], ...]]`, `woods [[lat, lon, rx_m, ry_m]]`
  - `water {rivers: [{p, w}], lakes: [[[lat, lon], ...]], labels: {name: [lat, lon]}}`
  - `camps [{a, b, rows, until}]`

## Testing
- **Preview server:** the `battle-library` entry in `~/.claude/launch.json` serves `dist/` on port 8791. Open `/preview.html#<id>`.
- **Portable release:** `dist/battle-atlas-offline.html` is a self-contained file. It embeds the Austerlitz, Rossbach and Cannae data, the available historical-map overlays, and the pinned Three.js 0.147 runtime; it can be copied or opened without sibling `battles/` files or a network connection.
- **Pass-through check:** load `/preview.html#<id>.p0`, then run `window.__atlas.passThrough()` in the console. It lists enemy units that end up behind each other after a move. Fix each one in the data, or confirm it is a real overrun. On screen, enemy blocks press against each other at contact (a routing unit gets shoved aside) with orange flashes, so they never share ground.
- **Hash changes need a reload:** changing only the `#id` part of the URL doesn't reload the page, so reload after switching battles that way.
- **Hidden panes look frozen:** a hidden browser pane throttles animation to about 1 frame per second, so wait before taking screenshots.
- **Python SSL is broken on Nathan's machine.** All network calls use `curl` through `subprocess`.

## Georeferencing source maps
- **What it does:** `battles/austerlitz/georef.py` fits an affine transform from pixel positions on a source map to latitude and longitude, using village control points.
- **Then:** the scenario can read positions straight off the map, e.g. `wp(1043, 766)` → Pratzen.
- **Check the residuals:** most should be under about 300 m. A large residual usually means a wrong place identification; at Austerlitz, Bosenitz turned out to be Tvarožná, not Podolí.
