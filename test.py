from PIL import Image
import shapes
from random import randint
import math
import pallet_maker

w = 5
h = 5
m = 100

img = Image.new("RGBA", (w * m, h * m), "white")
pxs = img.load()

pallet = pallet_maker.mix_pallet(w * h, (255,255,255))

for x in range(w * m):
    for y in range(h * m):
        pxs[x, y] = pallet[w * (y / m) + (x / m)]




img.save("test.png", "PNG")
