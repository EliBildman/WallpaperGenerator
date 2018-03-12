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

def in_any(shapes, point):
    for shape in shapes:
        if shape.contains_point(point):
            return True
    return False

def find_recs(w, h, max_size):
    recs = []
    open_points = points_open(w, h, recs)
    while len(open_points) > 0:
        point = open_points[randint(0, len(open_points) - 1)]
        end = point
        while not in_any(recs, end) and end[0] - point[0] <= max_size and end[0] < w:
            end = (end[0] + 1, end[1])
        end = (end[0] - 1, end[1])
        while not in_any(recs, end) and end[1] - point[1] <= max_size and end[1] < h:
            end = (end[0], end[1] + 1)
        end = (end[0], end[1] - 1)
        recs.append(Rectangle(point, end))



w = 100
h = 100

img = Image.new("RGBA", (w, h), "white")
pxs = img.load()

recs = find_recs(w, h, w/2)
for rec in recs:
    rec.outline(pxs)

img.save("test.png", "PNG")
