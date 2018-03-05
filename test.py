from PIL import Image
from shapes import Line_Seg, Triangle, NGon
from random import randint

w = 500
h = 500

t1 = Triangle((randint(0,w-1), randint(0,h-1)), (randint(0,w-1), randint(0,h-1)), (randint(0,w-1), randint(0,h-1)))
t2 = Triangle((randint(0,w-1), randint(0,h-1)), (randint(0,w-1), randint(0,h-1)), (randint(0,w-1), randint(0,h-1)))

img = Image.new("RGBA", (w, h), "green" if t1.collides_with(t2) else "red")
pxs = img.load()
t1.outline(pxs)
t2.outline(pxs)
img.save("test.png", "PNG")
