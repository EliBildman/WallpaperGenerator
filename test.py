from PIL import Image
from shapes import Line_Seg, Triangle, NGon
from random import randint

w = 50
h = 50


t = Triangle((0,0), (25, 25), (25, 0))

img = Image.new("RGBA", (w, h), "white")
pxs = img.load()
#t.fill(pxs, (255, 0, 0))
t.outline(pxs)
t.contains_point((15, 5))
pxs[15, 5] = (255, 0, 0)
#pxs[49,49] = (255,0,0)
# t1.outline(pxs)
# t2.outline(pxs)
img.save("test.png", "PNG")
