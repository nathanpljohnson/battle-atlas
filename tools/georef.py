"""Georeference source maps against known places.

usage: python3 tools/georef.py battles/<id> [--overlays]

battles/<id>/maps.json:
  {"<map_id>": {"file": "sources/x.png", "label": "West Point map 23 (09:00)", "order": 1,
                "gcps": {"Telnitz": [762, 1099], ...},      # place name (from places.json) -> pixel x, y
                "overlay": true}}                           # also warp into a terrain overlay
Writes battles/<id>/georef.json (transforms + residual report) and, with --overlays,
battles/<id>/overlay_<map_id>.webp aligned to the terrain bbox (transparent outside the map).

In scenario.py:  from georef import Georef;  G = Georef(HERE);  G.xy("wp23", 1043, 766) -> (lat, lon)
"""
import json, math, os, sys
import numpy as np

KM = 111200


def _terms(x, y, order):
    x = np.asarray(x, float); y = np.asarray(y, float)
    cols = [np.ones_like(x), x, y]
    if order >= 2:
        cols += [x * x, x * y, y * y]
    return np.stack(cols, axis=-1)


def fit(src, dst, order):
    """Least-squares polynomial map src (N,2) -> dst (N,2). Returns coefficient matrix."""
    A = _terms(src[:, 0], src[:, 1], order)
    coef, *_ = np.linalg.lstsq(A, dst, rcond=None)
    return coef


def apply(coef, x, y, order):
    return _terms(x, y, order) @ coef


class Georef:
    def __init__(self, bdir):
        self.bdir = bdir
        p = os.path.join(bdir, "georef.json")
        if not os.path.exists(p):
            raise SystemExit(f"run: python3 tools/georef.py {bdir}")
        self.maps = json.load(open(p))

    def xy(self, map_id, x, y):
        m = self.maps[map_id]
        la, lo = apply(np.array(m["fwd"]), x, y, m["order"])
        return (round(float(la), 5), round(float(lo), 5))

    def __call__(self, map_id):
        return lambda x, y: self.xy(map_id, x, y)


def main(bdir, overlays=False):
    maps = json.load(open(os.path.join(bdir, "maps.json")))
    places = json.load(open(os.path.join(bdir, "places.json")))
    out, report = {}, ["# Georeference report", ""]
    for mid, m in maps.items():
        order = m.get("order", 1)
        names = [n for n in m["gcps"] if n in places]
        missing = [n for n in m["gcps"] if n not in places]
        src = np.array([m["gcps"][n] for n in names], float)
        dst = np.array([places[n][:2] for n in names], float)
        need = 6 if order >= 2 else 3
        if len(names) < need + 1:
            raise SystemExit(f"{mid}: need at least {need + 1} control points for order {order}, have {len(names)}")
        lat0 = dst[:, 0].mean(); kx = KM * math.cos(math.radians(lat0))
        coef = fit(src, dst, order)
        res = []
        for i, n in enumerate(names):
            la, lo = apply(coef, src[i, 0], src[i, 1], order)
            res.append((n, float(math.hypot((la - dst[i, 0]) * KM, (lo - dst[i, 1]) * kx))))
        # leave-one-out residuals catch misidentified places better than in-sample ones
        loo = []
        for i, n in enumerate(names):
            keep = [j for j in range(len(names)) if j != i]
            c = fit(src[keep], dst[keep], order)
            la, lo = apply(c, src[i, 0], src[i, 1], order)
            loo.append(float(math.hypot((la - dst[i, 0]) * KM, (lo - dst[i, 1]) * kx)))
        med = float(np.median(loo))
        flags = [n for (n, _), e in zip(res, loo) if e > max(600, 3 * med)]
        inv = fit(dst, src, order)
        rmse = float(math.sqrt(np.mean([e * e for _, e in res])))
        mpp = float(math.hypot(coef[1, 0] * KM, coef[1, 1] * kx))
        out[mid] = {"label": m.get("label", mid), "file": m["file"], "order": order, "fwd": coef.tolist(), "inv": inv.tolist(),
                    "rmse_m": round(rmse), "m_per_px": round(mpp, 2),
                    "residuals_m": {n: round(e) for n, e in res}, "loo_m": {n: round(e) for n, e in zip(names, loo)}, "flagged": flags}
        report += [f"## {mid}: {m.get('label', mid)}", f"order {order}, {len(names)} control points, RMSE {rmse:.0f} m, {mpp:.1f} m/pixel", "",
                   "| place | residual m | leave-one-out m |", "|---|---|---|"]
        report += [f"| {n} | {e:.0f} | {l:.0f}{'  **CHECK**' if n in flags else ''} |" for (n, e), l in zip(res, loo)]
        if missing: report += ["", f"Missing from places.json: {', '.join(missing)}"]
        if flags: report += ["", f"**Flagged** (leave-one-out error > max(600 m, 3 × median)): {', '.join(flags)}. Usually a wrong place identification or a moved village."]
        report.append("")
        print(f"{mid}: order {order}, {len(names)} pts, RMSE {rmse:.0f} m, {mpp:.1f} m/px" + (f", FLAGGED {flags}" if flags else ""))
    json.dump(out, open(os.path.join(bdir, "georef.json"), "w"), indent=1)
    open(os.path.join(bdir, "georef_report.md"), "w").write("\n".join(report))
    if overlays:
        warp_all(bdir, maps, out)


def warp_all(bdir, maps, geo):
    from PIL import Image
    T = json.load(open(os.path.join(bdir, "terrain_config.json")))
    W, S, E, N = T["bbox"]
    kx = KM * math.cos(math.radians((S + N) / 2))
    OW = 2048; OH = round(OW * (N - S) * KM / ((E - W) * kx))
    for mid, m in maps.items():
        if not m.get("overlay"):
            continue
        g = geo[mid]
        im = Image.open(os.path.join(bdir, m["file"])).convert("RGB")
        a = np.asarray(im)
        yy, xx = np.mgrid[0:OH, 0:OW]
        lat = N - (yy + 0.5) / OH * (N - S); lon = W + (xx + 0.5) / OW * (E - W)
        sxy = apply(np.array(g["inv"]), lat, lon, g["order"])
        sx, sy = sxy[..., 0], sxy[..., 1]
        crop = m.get("crop")  # optional [x0, y0, x1, y1] of the map body, to drop margins and legends
        x0, y0, x1, y1 = crop if crop else (0, 0, a.shape[1], a.shape[0])
        inside = (sx >= x0) & (sx < x1 - 1) & (sy >= y0) & (sy < y1 - 1)
        ix = np.clip(sx.astype(int), 0, a.shape[1] - 1); iy = np.clip(sy.astype(int), 0, a.shape[0] - 1)
        rgba = np.zeros((OH, OW, 4), np.uint8)
        rgba[..., :3] = a[iy, ix]; rgba[..., 3] = np.where(inside, 255, 0)
        path = os.path.join(bdir, f"overlay_{mid}.webp")
        Image.fromarray(rgba).save(path, "WEBP", quality=72)
        print(f"overlay {path} ({os.path.getsize(path) // 1024} KB)")


if __name__ == "__main__":
    main(sys.argv[1], "--overlays" in sys.argv)
