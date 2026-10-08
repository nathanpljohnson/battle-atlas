"""Georeference the West Point Austerlitz maps (1920 px wide series) with village control points.
pix(x, y) -> (lat, lon) via least-squares affine. Usage: from georef import wp"""
import json, numpy as np
P = json.load(open("places_raw.json"))
GCP = {"Telnitz": (762, 1099), "Sokolnitz castle": (791, 972), "Kobelnitz": (885, 785), "Puntowitz": (912, 669),
       "Schlappanitz": (830, 559), "Pratzen": (1043, 766), "Krzenowitz": (1398, 752), "Austerlitz": (1660, 653),
       "Satschan": (849, 1195), "Menitz": (640, 1268), "Raigern": (162, 1207), "Bosenitz": (1095, 333),
       "Welatitz": (987, 280), "Posoritz post": (1386, 377)}
names = list(GCP)
A = np.array([[GCP[n][0], GCP[n][1], 1] for n in names], float)
Y = np.array([P[n] for n in names], float)
coef, *_ = np.linalg.lstsq(A, Y, rcond=None)
def wp(x, y):
    la, lo = np.array([x, y, 1.0]) @ coef
    return (round(float(la), 5), round(float(lo), 5))
if __name__ == "__main__":
    kx = 111200 * np.cos(np.radians(49.14))
    for n in names:
        la, lo = wp(*GCP[n]); e = np.hypot((la - P[n][0]) * 111200, (lo - P[n][1]) * kx)
        print(f"{n:18s} residual {e:5.0f} m")
    print("metres per pixel ~", round(float(np.hypot(coef[0][0] * 111200, coef[0][1] * kx)), 1))
