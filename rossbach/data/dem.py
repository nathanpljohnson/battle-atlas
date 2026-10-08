import math, subprocess, io, json
import numpy as np
from PIL import Image
W,E,S,N = 11.800, 11.990, 51.215, 51.292
Z = 13
def tile(lon, lat):
    n = 2**Z
    x = (lon+180)/360*n
    y = (1-math.asinh(math.tan(math.radians(lat)))/math.pi)/2*n
    return x, y
x0,y0 = tile(W,N); x1,y1 = tile(E,S)
tx0,ty0,tx1,ty1 = int(x0),int(y0),int(x1),int(y1)
mosaic = np.zeros(((ty1-ty0+1)*256,(tx1-tx0+1)*256))
for tx in range(tx0,tx1+1):
    for ty in range(ty0,ty1+1):
        url=f"https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{Z}/{tx}/{ty}.png"
        b = subprocess.run(["curl","-s",url],capture_output=True).stdout
        a = np.asarray(Image.open(io.BytesIO(b)).convert("RGB")).astype(float)
        h = a[...,0]*256 + a[...,1] + a[...,2]/256 - 32768
        mosaic[(ty-ty0)*256:(ty-ty0+1)*256,(tx-tx0)*256:(tx-tx0+1)*256] = h
# crop to bbox
px0=int((x0-tx0)*256); px1=int((x1-tx0)*256); py0=int((y0-ty0)*256); py1=int((y1-ty0)*256)
crop = mosaic[py0:py1, px0:px1]
np.save("dem_raw.npy", crop)
print(crop.shape, crop.min(), crop.max(), np.percentile(crop,[1,5,50,95,99]))
img = ((crop-crop.min())/(crop.max()-crop.min())*255).astype(np.uint8)
Image.fromarray(img).resize((crop.shape[1]*2//2, crop.shape[0])).save("dem_preview.png")
