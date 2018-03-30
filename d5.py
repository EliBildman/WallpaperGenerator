import shapes
import pallet_maker
from PIL import Image


def find_sqrs(w, h):
    pos = (0,0)
    sqrs = []
    c = 2
    while len(sqrs) == 0 or not fills_screen(w, h, sqrs[-1]):
        c *= 2
        sqrs.append(shapes.Square(pos, c))
    return sqrs


def fills_screen(w, h, sqr):
    return 0 > sqr.center[0] - sqr.r and w <= sqr.center[0] + sqr.r and 0 >= sqr.center[1] - sqr.r and h <= sqr.center[1] + sqr.r

w = 50
h = 50
img = Image.new("RGBA", (w, h), "white")
pxs = img.load()
ss = find_sqrs(w, h)
p = pallet_maker.random_pallet(len(ss))
i = 0
for s in ss:
    s.fill(pxs, dems = (w, h), color = p[i])
    s.outline(pxs, dems = (w, h))
    i += 1

img.save("test.png", "PNG")
