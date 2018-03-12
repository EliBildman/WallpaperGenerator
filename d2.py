from shapes import Rectangle
from PIL import Image
from random import randint

def points_open(w, h, recs):
    points = []
    for x in range(w):
        for y in range(h):
            for r in recs:
                if r.contains_point((x, y)):
                    break
            points.append((x, y))
    return points

def find_recs(w, h):
    recs = []
    open_points = points_open(w, h, recs)
    while len(open_points) > 0:
        point = open_points[randint(0, len(open_points) - 1)]
        




w = 100
h = 100

img = Image.new("RGBA", (w, h), "white")
pxs = img.load()

r = Rectangle((25, 25), (75, 75))
r.fill(pxs, (0,0,255))
r.outline(pxs)

img.save("test.png", "PNG")
