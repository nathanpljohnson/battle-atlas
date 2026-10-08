"""Build a battle's heightmap from AWS Terrain Tiles.

usage: python3 tools/terrain.py battles/<id>

Reads battles/<id>/terrain_config.json:
  {"bbox": [W, S, E, N], "zoom": 13, "grid_w": 240,
   "masks": [{"lat":..,"lon":..,"rx_m":..,"ry_m":..,"why":".."}],   # modern features to smooth away (pits, dams, motorways)
   "bumps": [{"lat":..,"lon":..,"h_m":..,"sigma_m":..,"why":".."}],  # features to restore (+) or remove (-)
   "exag": 3.2}
Writes battles/<id>/terrain.json and preview PNGs (terrain_raw.png, terrain_filled.png with places overlaid if places.json exists).
"""
import io, json, math, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw

UA = "BattleAtlas/0.2 (https://claude.ai/; personal non-commercial history project)"

def blur(a, s):
    if s <= 0:
        return a
    r = int(3 * s)
    k = np.exp(-0.5 * (np.arange(-r, r + 1) / s) ** 2); k /= k.sum()
    p = np.pad(a, r, mode="edge")
    p = np.apply_along_axis(lambda v: np.convolve(v, k, "valid"), 1, p)
    return np.apply_along_axis(lambda v: np.convolve(v, k, "valid"), 0, p)

def fetch_dem(W, S, E, N, Z):
    def tile(lon, lat):
        n = 2 ** Z
        return (lon + 180) / 360 * n, (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n
    x0, y0 = tile(W, N); x1, y1 = tile(E, S)
    tx0, ty0, tx1, ty1 = int(x0), int(y0), int(x1), int(y1)
    mosaic = np.zeros(((ty1 - ty0 + 1) * 256, (tx1 - tx0 + 1) * 256))
    for tx in range(tx0, tx1 + 1):
        for ty in range(ty0, ty1 + 1):
            url = f"https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{Z}/{tx}/{ty}.png"
            b = subprocess.run(["curl", "-s", "--fail", url], capture_output=True).stdout
            a = np.asarray(Image.open(io.BytesIO(b)).convert("RGB")).astype(float)
            mosaic[(ty - ty0) * 256:(ty - ty0 + 1) * 256, (tx - tx0) * 256:(tx - tx0 + 1) * 256] = a[..., 0] * 256 + a[..., 1] + a[..., 2] / 256 - 32768
    return mosaic[int((y0 - ty0) * 256):int((y1 - ty0) * 256), int((x0 - tx0) * 256):int((x1 - tx0) * 256)]

def build_mask(cfg, shape, bbox, lat, lon, kx, ky):
    W, S, E, N = bbox; H, Wd = shape
    mask = np.zeros(shape, bool)
    for m in cfg.get("masks", []):
        if "raster" in m:
            r = np.asarray(Image.open(os.path.join(cfg["_dir"], m["raster"])).resize((Wd, H))) > 0
            mask |= blur(r.astype(float), 2) > 0.05
        elif "poly" in m:
            im = Image.new("L", (Wd, H), 0)
            ImageDraw.Draw(im).polygon([((lo - W) / (E - W) * Wd, (N - la) / (N - S) * H) for la, lo in m["poly"]], fill=255)
            pm = np.asarray(im) > 0
            buf = m.get("buffer_m", 60) / (((E - W) * kx) / Wd)
            if buf > 0:
                pm = blur(pm.astype(float), buf / 2) > 0.08
            mask |= pm
        else:
            mask |= ((lon - m["lon"]) * kx / m["rx_m"]) ** 2 + ((lat - m["lat"]) * ky / m["ry_m"]) ** 2 < 1
    return mask


def flood(allowed, seed):
    """Connected region of `allowed` reachable from `seed` pixels (4-neighbour)."""
    out = np.zeros_like(allowed); stack = list(zip(*np.nonzero(seed)))
    H, W = allowed.shape
    while stack:
        y, x = stack.pop()
        if y < 0 or x < 0 or y >= H or x >= W or out[y, x] or not allowed[y, x]: continue
        out[y, x] = True; stack += [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    return out


def hull(pts):
    """Convex hull (monotone chain) of (lat, lon) points."""
    pts = sorted(set(pts))
    if len(pts) < 3: return pts
    cross = lambda o, a, b: (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, up = [], []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0: lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0: up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


def stitch(ways):
    """Join multipolygon member ways that share end points into closed rings."""
    segs = [[(p["lat"], p["lon"]) for p in w] for w in ways if len(w) > 1]
    rings = []
    while segs:
        ring = segs.pop(0)
        changed = True
        while changed and ring[0] != ring[-1]:
            changed = False
            for i, sgm in enumerate(segs):
                if sgm[0] == ring[-1]: ring += sgm[1:]
                elif sgm[-1] == ring[-1]: ring += sgm[::-1][1:]
                elif sgm[-1] == ring[0]: ring = sgm[:-1] + ring
                elif sgm[0] == ring[0]: ring = sgm[::-1][:-1] + ring
                else: continue
                segs.pop(i); changed = True; break
        rings.append([{"lat": a, "lon": b} for a, b in ring])
    return rings


def overpass(bbox, cache=None):
    if cache and os.path.exists(cache) and "--refetch" not in sys.argv:
        return json.load(open(cache))
    W, S, E, N = bbox; b = f"({S},{W},{N},{E})"
    q = ("[out:json][timeout:90];("
         f'way["landuse"~"quarry|landfill|brownfield"]{b};way["man_made"~"spoil_heap|tailings"]{b};'
         f'way["natural"="water"]{b};relation["natural"="water"]{b};way["landuse"~"reservoir|basin"]{b};'
         f'way["highway"="motorway"]{b};);out geom;')
    import time
    for k in range(5):
        r = subprocess.run(["curl", "-s", "-A", UA, "--data-urlencode", "data=" + q, "https://overpass-api.de/api/interpreter"], capture_output=True, text=True)
        try:
            els = json.loads(r.stdout).get("elements", [])
            if cache: json.dump(els, open(cache, "w"))
            return els
        except json.JSONDecodeError:
            time.sleep(10 * (k + 1))
    raise SystemExit("Overpass API unavailable (rate limited); try again in a few minutes")


def detect(bdir, cfg, d, bbox):
    """Flag modern changes: OSM quarries/landfill/spoil (auto-masked), water bodies sunk well below the surrounding
    ground (flooded pits: auto-masked), other water and motorways (suggested only), and unexplained DEM pits/heaps."""
    W, S, E, N = bbox; H, Wd = d.shape
    kx = 111200 * math.cos(math.radians((S + N) / 2)); ky = 111200
    mpp = (E - W) * kx / Wd
    smooth = blur(d, 600 / mpp)
    anom = d - smooth
    to_px = lambda la, lo: ((lo - W) / (E - W) * Wd, (N - la) / (N - S) * H)
    feats = []
    pit_raster = np.zeros(d.shape, bool)
    for e in overpass(bbox, os.path.join(bdir, "osm_cache.json")):
        geoms = [e["geometry"]] if e["type"] == "way" and "geometry" in e else stitch([m["geometry"] for m in e.get("members", []) if m.get("role") == "outer" and "geometry" in m])
        tags = e.get("tags", {})
        for g in geoms:
            poly = [(p["lat"], p["lon"]) for p in g]
            if len(poly) < 3: continue
            xs = [(lo - W) * kx for la, lo in poly]; ys = [(la - S) * ky for la, lo in poly]
            area = abs(sum(xs[i] * ys[i - 1] - xs[i - 1] * ys[i] for i in range(len(xs)))) / 2
            im = Image.new("L", (Wd, H), 0); ImageDraw.Draw(im).polygon([to_px(*p) for p in poly], fill=255)
            inside = np.asarray(im) > 0
            depth = 0.0
            if inside.any():
                # compare the water/feature surface with a ring of land 200-700 m around it
                near = blur(inside.astype(float), 450 / mpp) > 0.02
                ring = near & ~(blur(inside.astype(float), 150 / mpp) > 0.02)
                if ring.sum() > 20:
                    depth = float(np.median(d[ring]) - np.median(d[inside]))
                else:
                    depth = float(-np.median(anom[inside]))
            kind = tags.get("landuse") or tags.get("man_made") or tags.get("highway") or tags.get("water") or tags.get("natural")
            if tags.get("highway") == "motorway":
                action = "suggest"; why = "motorway (embankments and cuttings)"
            elif kind in ("quarry", "landfill", "spoil_heap", "tailings", "brownfield"):
                action = "auto" if area > 20000 else "suggest"; why = f"OSM {kind}"
            elif depth > 8 and area > 20000:
                action = "auto"; why = f"water {depth:.0f} m below surrounding ground: likely flooded pit or quarry"
            else:
                action = "suggest" if area > 20000 else "ignore"; why = f"water body ({kind}); keep if it existed at the time"
            grown = None
            if action == "auto" and depth > 4:
                for thr, ratio in ((-6, 6), (-4, 15)):
                    seed = inside & (anom < thr)
                    region = flood(anom < thr, seed)
                    if 0 < region.sum() * mpp * mpp < ratio * max(area, 1):
                        grown = region if grown is None else (grown | region)
            if action != "ignore":
                feats.append({"action": action, "why": why, "name": tags.get("name", ""), "area_ha": round(area / 1e4, 1),
                              "depth_m": round(depth, 1), "poly": [[round(a, 5), round(b, 5)] for a, b in poly[:: max(1, len(poly) // 120)]], "grown": grown is not None})
                if grown is not None:
                    pit_raster |= grown
    # unexplained anomalies (pits/heaps) not covered by OSM features
    anom2 = d - blur(d, 1000 / mpp)
    big = np.abs(blur(anom2, 2)) > 15
    covered = build_mask({"_dir": bdir, "masks": [{"poly": f["poly"], "buffer_m": 150} for f in feats]}, d.shape, bbox,
                         None, None, kx, ky) if feats else np.zeros_like(big)
    loose = big & ~covered
    blobs = []
    if loose.any():
        lbl = np.zeros(loose.shape, int); n = 0
        ys, xs = np.nonzero(loose)
        seen = np.zeros_like(loose)
        for y0, x0 in zip(ys[::25], xs[::25]):
            if seen[y0, x0]: continue
            stack = [(y0, x0)]; pts = []
            while stack and len(pts) < 200000:
                y, x = stack.pop()
                if y < 0 or x < 0 or y >= H or x >= Wd or seen[y, x] or not loose[y, x]: continue
                seen[y, x] = True; pts.append((y, x)); stack += [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
            a_ha = len(pts) * mpp * mpp / 1e4
            if 2 < a_ha < 300:
                py, px = np.mean(pts, axis=0); mv = float(np.mean([anom2[p] for p in pts[:2000]]))
                blobs.append({"lat": round(N - py / H * (N - S), 5), "lon": round(W + px / Wd * (E - W), 5),
                              "area_ha": round(a_ha, 1), "mean_m": round(mv, 1), "sign": "pit" if mv < 0 else "heap", "score": abs(mv) * a_ha})
    blobs = sorted(blobs, key=lambda b: -b["score"])[:8]
    json.dump({"features": feats, "dem_anomalies": blobs}, open(os.path.join(bdir, "terrain_suggestions.json"), "w"), indent=1)
    Image.fromarray((pit_raster * 255).astype(np.uint8)).save(os.path.join(bdir, "terrain_automask.png"))
    cfg["masks"] = [m for m in cfg.get("masks", []) if not m.get("auto")] + (
        [{"raster": "terrain_automask.png", "auto": True, "why": "flooded pits grown from OSM water bodies (exact shape)"}] if pit_raster.any() else []) + [
        {"poly": f["poly"], "buffer_m": 80, "auto": True, "why": f["why"] + (f" ({f['name']})" if f["name"] else "")} for f in feats if f["action"] == "auto"]
    json.dump(cfg, open(os.path.join(bdir, "terrain_config.json"), "w"), indent=1, ensure_ascii=False)
    im = Image.fromarray(((d - d.min()) / max(1e-6, d.max() - d.min()) * 255).astype(np.uint8)).convert("RGB")
    dr = ImageDraw.Draw(im)
    for f in feats:
        dr.polygon([to_px(*p) for p in f["poly"]], outline=(255, 40, 40) if f["action"] == "auto" else (255, 210, 0), width=3)
    for b in blobs:
        x, y = to_px(b["lat"], b["lon"]); dr.ellipse([x - 12, y - 12, x + 12, y + 12], outline=(0, 200, 255), width=3)
    im.save(os.path.join(bdir, "terrain_detect.png"))
    na = sum(f["action"] == "auto" for f in feats)
    print(f"detect: {na} auto-masked, {len(feats) - na} suggested, {len(blobs)} unexplained DEM pits/heaps -> terrain_suggestions.json, terrain_detect.png")


def main(bdir):
    cfg = json.load(open(os.path.join(bdir, "terrain_config.json")))
    W, S, E, N = cfg["bbox"]
    raw_path, key_path = os.path.join(bdir, "terrain_raw.npy"), os.path.join(bdir, "terrain_raw.key")
    key = json.dumps([cfg["bbox"], cfg.get("zoom", 13)])
    if os.path.exists(raw_path) and os.path.exists(key_path) and open(key_path).read() == key:
        d = np.load(raw_path)
    else:
        d = fetch_dem(W, S, E, N, cfg.get("zoom", 13))
        np.save(raw_path, d); open(key_path, "w").write(key)
    H, Wd = d.shape
    yy, xx = np.mgrid[0:H, 0:Wd]
    lon = W + (xx + 0.5) / Wd * (E - W); lat = N - (yy + 0.5) / H * (N - S)
    kx = 111200 * math.cos(math.radians((S + N) / 2)); ky = 111200
    if "--detect" in sys.argv:
        detect(bdir, cfg, d, (W, S, E, N))
        cfg = json.load(open(os.path.join(bdir, "terrain_config.json")))
    cfg["_dir"] = bdir
    mask = build_mask(cfg, d.shape, (W, S, E, N), lat, lon, kx, ky)
    f = d.copy()
    if mask.any():
        w = (~mask).astype(float); est = None
        for s in (60, 30, 15):
            num = blur(np.where(mask, 0, d) * w, s); den = blur(w, s)
            e = num / np.maximum(den, 1e-6)
            est = e if est is None else np.where(den > 0.35, e, est)
        f = np.where(mask, est, d)
        m2 = np.clip(blur(mask.astype(float), 10) * 1.6, 0, 1)
        f = d * (1 - m2) + f * m2
    for b in cfg.get("bumps", []):
        dx = (lon - b["lon"]) * kx; dy = (lat - b["lat"]) * ky
        f = f + b["h_m"] * np.exp(-(dx * dx + dy * dy) / (2 * b["sigma_m"] ** 2))
    GW = cfg.get("grid_w", 240)
    GH = max(2, round(GW * (N - S) * ky / ((E - W) * kx)))
    g = np.asarray(Image.fromarray(f.astype(np.float32)).resize((GW, GH), Image.BILINEAR))
    g = blur(g, cfg.get("blur", 0.8))
    gmin = float(g.min())
    out = {"w": GW, "h": GH, "bbox": [W, S, E, N], "min": gmin, "max": float(g.max()), "exag": cfg.get("exag", 3.2),
           "z": [int(round((v - gmin) * 10)) for v in g.ravel()]}
    json.dump(out, open(os.path.join(bdir, "terrain.json"), "w"))
    for name, arr in (("terrain_raw.png", d), ("terrain_filled.png", f)):
        im = Image.fromarray(((arr - arr.min()) / max(1e-6, arr.max() - arr.min()) * 255).astype(np.uint8)).convert("RGB")
        pf = os.path.join(bdir, "places.json")
        if os.path.exists(pf):
            dr = ImageDraw.Draw(im)
            for k, v in json.load(open(pf)).items():
                x = (v[1] - W) / (E - W) * Wd; y = (N - v[0]) / (N - S) * H
                dr.ellipse([x - 4, y - 4, x + 4, y + 4], fill=(255, 0, 0)); dr.text((x + 6, y - 6), k, fill=(255, 255, 0))
        im.save(os.path.join(bdir, name))
    print(f"terrain {GW}x{GH}, elevation {out['min']:.0f}-{out['max']:.0f} m, masks {len(cfg.get('masks', []))}, bumps {len(cfg.get('bumps', []))}")

if __name__ == "__main__":
    main(sys.argv[1])
