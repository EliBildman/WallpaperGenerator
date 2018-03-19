from PIL import Image
import shapes
from random import randint
import math
import pallet_maker

w = 500
h = 500

img = Image.new("RGBA", (w, h), "white")
pxs = img.load()

s = shapes.NGon((10,10), (250, 490), (490, 490), (490, 10))
s.outline(pxs, thickness = 2)



img.save("test.png", "PNG")
