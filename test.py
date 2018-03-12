from PIL import Image
from shapes import Line_Seg, Triangle, NGon
from random import randint

w = 50
h = 50


t = Triangle((25,0), (49, 0), (49, 25))

img = Image.new("RGBA", (w, h), "white")
pxs = img.load()
t.fill(pxs, (255, 0, 0))
print t.contains_point((25, 0))
#pxs[49,49] = (255,0,0)
# t1.outline(pxs)
# t2.outline(pxs)
img.save("test.png", "PNG")
