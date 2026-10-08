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
    mask = np.zeros_like(d, bool)
    for m in cfg.get("masks", []):
        mask |= ((lon - m["lon"]) * kx / m["rx_m"]) ** 2 + ((lat - m["lat"]) * ky / m["ry_m"]) ** 2 < 1
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
