from PIL import Image
import shapes
from random import randint
import math
import pallet_maker
import helpers

w = 10
h = 1

img = Image.new("RGBA", (w, h), "white")
pxs = img.load()

for i in range(0, 360, 36):
    pxs[i / 36, 0] = helpers.to_rgb((i, 1, 1))



img.save("test.png", "PNG")
