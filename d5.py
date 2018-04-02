import shapes
import pallet_maker
import random
from PIL import Image


def find_sqrs(w, h):
    sqrs = []
    s = 2
    while len(sqrs) == 0 or not fills_screen(w, h, sqrs[-1]) or not (0 <= sqrs[-1].center[0] < w and 0 <= sqrs[-1].center[1] < h):
        pos = pos = (random.randint(w/3, 2*w/3), random.randint(h/3, 2*h/3)) if len(sqrs) == 0 else sqrs[-1].center
        s = int(s * (random.random() * 2 + 1.5))
        offset = tuple(random.randint(-1 * (s/2) - sqrs[-1].l, (s/2) - sqrs[-1].l) for i in range(2)) if len(sqrs) > 0 else (0,0)
        sqrs.append(shapes.Square((pos[0] + offset[0], pos[1] + offset[1]), s))
        print
    return sqrs[:-1]


def fills_screen(w, h, sqr):
    return 0 > sqr.center[0] - (sqr.l / 2) and w <= sqr.center[0] + (sqr.l / 2) and 0 >= sqr.center[1] - (sqr.l / 2) and h <= sqr.center[1] + (sqr.l / 2)

w = 200
h = 200
ss = find_sqrs(w, h)
p = pallet_maker.close_pallet(len(ss) + 1)
img = Image.new("RGBA", (w, h), p[0])
pxs = img.load()
i = 1
for s in ss[::-1]:
    print str(i) + "/" + str(len(ss))
    s.fill(pxs, dems = (w, h), color = p[i])
    s.outline(pxs, dems = (w, h), thickness = int(s.r ** 0.5) / 5)
    i += 1

img.save("test.png", "PNG")
