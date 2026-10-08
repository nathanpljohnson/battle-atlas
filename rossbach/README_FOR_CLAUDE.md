# Rossbach 1757: interactive 3D battle map

A single-page interactive map of the Battle of Rossbach (5 November 1757, Seven Years' War), in the style of the Osprey "Campaign" bird's-eye views. It shows real terrain as a tilted 3D slab, with unit blocks for infantry, cavalry, artillery and light troops. A timeline steps through ten moments from 09:00 to 16:45, and units animate between positions and formations. Each moment has movement, charge, retreat and fire arrows, numbered events, narrative and tactics notes, and sun and dusk lighting for the real date.

## For a human: quick start

- **To just look at it:** open `preview.html` in a web browser (Chrome, Safari, Firefox, Edge). It needs an internet connection the first time, because it loads three.js and fonts from public CDNs. Everything else is built into the file.
- **To change the battle and rebuild:** see "Rebuild pipeline" below. You need Python 3 with `numpy` and `Pillow`, plus `curl`.
- **To hand it to Claude:** give Claude this whole folder and say "read README_FOR_CLAUDE.md first".

---

## For a Claude agent: read this first

You are being given the full source of a working project. Don't rebuild from scratch. The pipeline below regenerates everything. Read this file, then `RESUME.md` (the original author's handoff notes, which mention paths on their machine), then `data/scenario.py`.

### File map

| Path | What it is | Edit? |
|---|---|---|
| `src.html` | The page template: HTML, CSS and all JavaScript (three.js r147 + OrbitControls UMD from CDNs). It has three placeholders: `/*SCENARIO*/null`, `/*HMETA*/null` and `/*HEIGHT*/`. | Yes, for UI, rendering and styling |
| `build.py` | Inlines `data/scenario.json` and `data/height.json` into `src.html`, and writes `rossbach.html` and `preview.html`. | Rarely |
| `rossbach.html` | **Build output.** A body fragment with no `<!doctype>`, `<html>` or `<head>`, made for publishing as a claude.ai Artifact (the host adds the skeleton). | Never by hand |
| `preview.html` | **Build output.** The same page wrapped in a full HTML document, for opening locally or hosting anywhere. | Never by hand |
| `data/scenario.py` | **All battle content:** units, their position, facing and formation at each phase, arrows, numbered events, narrative and tactic text, village coordinates, roads and woods. Writes `data/scenario.json`. | Yes, for content |
| `data/scenario.json` | Generated from `scenario.py`. | Never by hand |
| `data/dem.py` | Downloads elevation tiles (AWS Terrain Tiles, "terrarium" PNG encoding, zoom 13) for the bounding box and writes `data/dem_raw.npy`. | Only for a new area |
| `data/fill.py` | Smooths over the modern lignite-mining pits, adds back the Janus and Polzen hills (Gaussian bumps), downsamples to a 240×156 grid and writes `data/height.json`. Also writes `dem_filled.png`. | Only for a new area |
| `data/height.json` | Heightmap: `{w, h, bbox:[W,S,E,N], min, max, z:[...]}`, with `z` = (elevation − min) × 10 as integers, row-major, north row first. | Generated |
| `data/geocode.py`, `data/places.json` | Village coordinates from OpenStreetMap Nominatim, used once to fill in `places` in `scenario.py`. | Reference |
| `data/*.png` | Debug images: elevation previews, and `phases_check.png`, a 2D plot of every unit in every phase. | Reference |
| `RESUME.md`, `tasks/todo.md` | The original author's handoff notes and checklist. | Reference |

`data/dem_raw.npy` (6 MB) is **not included**. Run `data/dem.py` to regenerate it if you need to rerun `fill.py`. You don't need it just to edit content.

### Rebuild pipeline

Run from the project root:

```bash
cd data && python3 scenario.py && cd ..
python3 build.py
```

That's all you need after editing `scenario.py` or `src.html`. Only for new terrain:

```bash
cd data && python3 dem.py && python3 fill.py && cd ..
python3 build.py
```

Notes:
- The scripts in `data/` use **relative paths**. Run them from inside `data/`.
- The original machine's Python couldn't verify SSL certificates, so the network calls in `dem.py` and `geocode.py` go through `curl` via `subprocess`. That works anywhere `curl` exists.
- `fill.py` has the pit locations hard-coded as ellipses in **pixel coordinates of the raw elevation crop** (1107×717 pixels for this bounding box). If the bounding box changes, redo these by looking at `dem_preview.png`.
- Pillow warns that the `mode=` argument is deprecated. The script already avoids it.

### Data model (`data/scenario.py`)

- **Units:** each unit is `U(id, side, type, name, strength, frontage_m, keys, note)`.
  - `side`: `"pr"` (Prussia, blue), `"fr"` (France, white) or `"re"` (Reichsarmee/Austrian, red).
  - `type`: `"inf"`, `"cav"`, `"lc"` (light cavalry), `"art"` or `"lt"` (light infantry).
  - `strength`: a free-text string. The page reads the number of blocks from patterns like `"· 4 bns"` or `"· 10 sqns"`.
- **Keys:** `keys = {phase_index: (lat, lon, facing_deg, form)}`. Facing is a compass bearing (0 = north). `form` is one of:
  - `X`: camp
  - `C`: march column
  - `L`: line
  - `F`: firing line (draws musket smoke)
  - `R`: rout (scattered blocks)

  A phase with no key carries the previous key forward, so you only need to write keys when something changes.
- **Helpers:**
  - `mv(point, bearing, meters)` offsets a point.
  - `echelon(lead, facing, n, spacing, setback)` builds a stepped line.
- **Phases:** each entry in `phases` is `{t, label, title, text, tactic:(heading, body), arrows:[{s: side, k: move|charge|retreat|fire, p: [[lat, lon], ...]}], events:[[lat, lon, text]]}`.
- **Commanders:** `hq` holds commanders' flags, with keys `{phase: (lat, lon)}`.
- **Scenery:**
  - `places`: `{name: [lat, lon]}`. Each place gets a label and 3D houses.
  - `hills`: label-only entries.
  - `roads`: lists of place names, joined in order.
  - `woods`: `[lat, lon, rx_m, ry_m]`.
- **Unit codes:** the page gives Prussian units letters (A, B, …) and allied units numbers (1, 2, …), in the order they appear in the data.

After editing, it helps to regenerate a 2D check plot like `data/phases_check.png`. The code that made it was a throwaway snippet, so rewrite it if you need it: draw each unit as a line over `dem_filled.png`, one panel per phase. It catches geography mistakes much faster than the 3D view.

### Page and rendering facts (`src.html`)

- **Coordinates:** world units are kilometres. x = east, z = south (north is −z), y = up. Use `xz(lat, lon)` and `hAt(x, z)`.
- **Constants:**
  - `EXAG = 3.2`: vertical exaggeration.
  - `SC = 1.9`: unit block size multiplier (blocks are deliberately larger than real life).
  - `FOCUS[]`: the camera target and distance for each phase.
  - The camera's starting view is from the south-south-west.
- **Terrain texture:** painted on a 2048-pixel canvas at load. It combines an elevation tint and hillshade, open-field strips, woods, village grounds and roads.
- **Animation:** units tween over 1.5 s, arrows draw on over 1.2 s and the camera flies over 1.6 s. The frame delta is capped at 0.25 s.
- **Lighting:** `sunAt()` computes sun altitude and azimuth for 51.25°N with a declination of −15.6°. The directional light, hemisphere light and a CSS dusk overlay (`--dusk`) follow it.
- **Theme:** colors use CSS tokens, with light and dark sets. The page follows `prefers-color-scheme` and `data-theme`.

### Publishing

- **As a claude.ai Artifact:**
  1. Load the artifact-design guidance.
  2. Publish `rossbach.html` (the fragment).
  3. Allowed script CDNs are cdnjs, jsdelivr and unpkg, which are what the page uses. No other network fetches are allowed, which is why all the data is inlined.
- **Anywhere else** (GitHub Pages, Netlify, a local file): use `preview.html`.

### Testing

- **Local server:** serve the folder with `python3 -m http.server 8790` and open `/preview.html`. Opening the file directly also works.
- **Hidden previews look frozen:** a hidden or background browser tab throttles `requestAnimationFrame` to about 1 frame per second. Screenshots from a hidden preview pane can therefore show units that haven't moved yet. Don't mistake that for a bug: check `document.visibilityState`.
- **What to check:** no console errors, no sideways scrolling at 375 px wide, both themes, and phases 0, 4 (15:30, the charge) and 6 (16:00, the infantry fight).

### Making a different battle

1. Choose a bounding box, then update `W, E, S, N` in `dem.py` and the bbox in `fill.py`. `fill.py` also hard-codes the bbox when it computes the hill bumps: the `11.800` / `0.190` / `51.292` / `0.077` constants.
2. Remove or redo the pit ellipses and hill bumps in `fill.py`. They are specific to Rossbach.
3. Geocode the villages (`geocode.py`, using the Nominatim usage policy: 1 request per second with a real User-Agent).
4. Rewrite `scenario.py`.
5. Edit the hard-coded text in `src.html`: title, header, the forces bars in `renderForces()` and the source notes. Also update `FOCUS[]`, and the latitude and declination in `sunAt()` for the new date and place.

### Accuracy caveats (keep them in the page)

- Unit positions are an approximate reconstruction from standard accounts. Timings follow Simon Millar, *Rossbach and Leuthen 1757* (Osprey Campaign 113).
- The terrain is modern elevation data. The 20th-century mining pits are smoothed out and the Janus and Polzen hills are restored by estimate.
- Roads, woods and village outlines are illustrative, not taken from historical maps.
