from PIL import Image
from shapes import Line_Seg, Triangle, NGon
from random import randint

w = 50
h = 50

s = NGon((5, 5), (5, 45), (45, 45), (45, 5))

# t1 = NGon([(10, 10), (250, 10), (249, 249), (10, 250)])
# t2 = NGon([(250, 250), (490, 250), (490, 490), (250, 490)])
#
# img = Image.new("RGBA", (w, h), "green" if t1.collides_with(t2) else "red")
# pxs = img.load()
# t1.outline(pxs)
# t2.outline(pxs)
img.save("test.png", "PNG")
