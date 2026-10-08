import numpy as np, json
from PIL import Image
d = np.load("dem_raw.npy"); H,W = d.shape
def blur(a, s):
    r = int(3*s); k = np.exp(-0.5*(np.arange(-r,r+1)/s)**2); k/=k.sum()
    p = np.pad(a, r, mode="edge")
    p = np.apply_along_axis(lambda v: np.convolve(v,k,"valid"), 1, p)
    p = np.apply_along_axis(lambda v: np.convolve(v,k,"valid"), 0, p)
    return p
yy,xx = np.mgrid[0:H,0:W]
mask = np.zeros_like(d,bool)
def ell(cx,cy,rx,ry): return ((xx-cx)/rx)**2+((yy-cy)/ry)**2<1
mask |= ell(815,140,132,190)     # Runstedter See pit NE
mask |= ell(648,420,108,98)       # pit south of Lunstaedt
mask |= ell(628,338,42,38)       # small pit
mask |= ell(655,70,60,45)        # spoil heap
mask |= ell(487,395,30,50)       # spoil heap
mask |= ell(530,8,60,20)
mask |= ell(735,25,35,30)
f = d.copy()
w = (~mask).astype(float)
est = None
for s in (60,30,15):
    num = blur(np.where(mask,0,d)*w, s); den = blur(w, s)
    e = num/np.maximum(den,1e-6)
    est = e if est is None else np.where(den>0.35, e, est)
f = np.where(mask, est, d)
# feather edges
m2 = np.clip(blur(mask.astype(float), 10)*1.6,0,1)
f = d*(1-m2) + f*m2
lon = 11.800 + xx/W*0.190; lat = 51.292 - yy/H*0.077
def bump(la,lo,hm,sig_m):
    dx=(lon-lo)*69600; dy=(lat-la)*111200
    return hm*np.exp(-(dx*dx+dy*dy)/(2*sig_m**2))
base = blur(f, 40)
f = np.where(mask, f, f) + bump(51.2666,11.9333,16,520) + bump(51.2712,11.9545,11,450)
# downsample to grid for the page
GW, GH = 240, 156
img = Image.fromarray(f.astype(np.float32), ).resize((GW,GH), Image.BILINEAR)
g = np.asarray(img)
g = blur(g, 0.8)
print(g.min(), g.max())
json.dump({"w":GW,"h":GH,"bbox":[11.800,51.215,11.990,51.292],"min":float(g.min()),"max":float(g.max()),
  "z":[int(round((v-g.min())*10)) for v in g.ravel()]}, open("height.json","w"))
prev = ((f-f.min())/(f.max()-f.min())*255).astype(np.uint8)
Image.fromarray(prev).save("dem_filled.png")
