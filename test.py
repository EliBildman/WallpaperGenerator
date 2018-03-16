from PIL import Image
import shapes
from random import randint
import math

w = 400
h = 400


r = shapes.Normal((200,200), 50, 100)

img = Image.new("RGBA", (w, h), "white")
pxs = img.load()
r.fill(pxs, (0, 0, 100))
#pxs[49,49] = (255,0,0)
# t1.outline(pxs)
# t2.outline(pxs)
img.save("test.png", "PNG")
