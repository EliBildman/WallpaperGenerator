import shapes
import pallet_maker
import random
from PIL import Image


def find_sqrs(w, h):
    pos = (random.randint(w/3, 2*w/3), random.randint(h/3, 2*h/3))
    sqrs = []
    c = 2
    while len(sqrs) == 0 or not fills_screen(w, h, sqrs[-1]):
        c = int(c * (random.random() * 2 + 1.5))
        sqrs.append(shapes.Square(pos, c))
    return sqrs[:-1]


def fills_screen(w, h, sqr):
    return 0 > sqr.center[0] - sqr.r and w <= sqr.center[0] + sqr.r and 0 >= sqr.center[1] - sqr.r and h <= sqr.center[1] + sqr.r

w = 1000
h = 500
ss = find_sqrs(w, h)
p = pallet_maker.mix_pallet(len(ss) + 1, (150, 150, 150))
img = Image.new("RGBA", (w, h), p[0])
pxs = img.load()
i = 1
for s in ss[::-1]:
    print str(i) + "/" + str(len(ss))
    s.fill(pxs, dems = (w, h), color = p[i])
    s.outline(pxs, dems = (w, h), thickness = int(s.r ** 0.5) / 5)
    i += 1

img.save("test.png", "PNG")
