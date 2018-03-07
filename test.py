from PIL import Image
from shapes import Line_Seg, Triangle, NGon
from random import randint

w = 50
h = 50


t = NGon([(10,10), (10, 40), (40, 10)])

img = Image.new("RGBA", (w, h), "white")
pxs = img.load()
t.outline(pxs)
# t1.outline(pxs)
# t2.outline(pxs)
img.save("test.png", "PNG")
