from shapes import Rectangle
from PIL import Image
from random import randint
import pallet_maker

def points_open(w, h, jump, recs):
    points = []
    for x in range(0, w, jump):
        for y in range(0, h, jump):
            op = True
            for r in recs:
                if r.contains_point((x + 1, y + 1)):
                    op = False
                    break
            if op:
                points.append((x, y))
    return points

def in_any(shapes, point):
    for shape in shapes:
        if shape.contains_point(point):
            return True
    return False

# def find_recs(w, h, min_size, max_size):
#     recs = []
#     open_points = points_open(w, h, min_size, recs)
#     while len(open_points) > 0:
#         point = open_points[randint(0, len(open_points) - 1)]
#         end = point
#         end = (end[0] + min_size, end[1])
#         while not in_any(recs, end) and end[0] - point[0] <= max_size:
#             end = (end[0] + min_size, end[1])
#         end = (end[0], end[1] + min_size)
#         while not in_any(recs, end) and not in_any(recs, (point[0], end[1])) and end[1] - point[1] <= max_size:
#             end = (end[0], end[1] + min_size)
#         if end[0] >= w:
#             end = (w - 1, end[1])
#         if end[1] >= h:
#             end = (end[0], h - 1)
#         recs.append(Rectangle(point, end))
#         open_points = points_open(w, h, min_size, recs)
#         print len(open_points)
#     return recs

def find_recs():
    


w = 1080
h = 1920

img = Image.new("RGBA", (w, h), "white")
pxs = img.load()

recs = find_recs(w, h, 50, w/2)
pallet = pallet_maker.spectrum_pallet(len(recs), 50)
for i in range(len(recs)):
    recs[i].fill(pxs, tuple(randint(0, 255) for x in range(3)))
    recs[i].outline(pxs)

img.save("test.png", "PNG")
