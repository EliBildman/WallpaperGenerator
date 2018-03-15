from PIL import Image
from shapes import Line_Seg, Triangle, NGon, Rectangle
from random import randint

w = 50
h = 50


r = Rectangle((1,1), (25, 25))

img = Image.new("RGBA", (w, h), "white")
pxs = img.load()
r.fill(pxs, (255, 0, 0))
#pxs[49,49] = (255,0,0)
# t1.outline(pxs)
# t2.outline(pxs)
img.save("test.png", "PNG")
