from PIL import Image
from shapes import Line_Seg, Triangle, NGon
from random import randint

w = 500
h = 500

l1 = Line_Seg((randint(0,w-1) - 2, randint(0,h-1)), (randint(0,w-1), randint(0,h-1)))
l2 = Line_Seg((randint(0,w-1), randint(0,h-1)), (randint(0,w-1), randint(0,h-1)))
img = Image.new("RGBA", (w, h), "green" if l1.collides_with(l2) else "red")
pxs = img.load()
l1.draw(pxs, thickness = 2)
l2.draw(pxs, thickness = 2)
img.save("test.png", "PNG")
