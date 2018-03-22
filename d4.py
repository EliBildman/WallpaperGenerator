import shapes
import random
from PIL import Image

def random_points(n, w, h):
    points = []
    for i in range(n):
        points.append(shapes.Point(random.randint(0, w - 1), random.randint(0, h - 1)))
    return points

def connect_points(points):
    lines = []
    for j in range(len(points)):
        point = points[j]
        for i in range(2 - len(point.lines)):
            o_ind = random.randint(0, len(points) - 1)
            while (o_ind == j) or (points[o_ind] in point.lines) or (any_collisions(shapes.Line_Seg(point.pos, points[o_ind].pos), lines)):
                o_ind = random.randint(0, len(points) - 1)
                #print (any_collisions(shapes.Line_Seg(point.pos, points[o_ind].pos), lines)), lines
            n_line = shapes.Line_Seg(point.pos, points[o_ind].pos)
            point.lines.append(n_line)
            lines.append(n_line)
    return lines

def any_collisions(curr_line, lines):
    for line in lines:
        if line.collides_with(curr_line):
            return True
    return False



w = 500
h = 500

img = Image.new("RGBA", (w, h), "white")
pxs = img.load()

points = random_points(100, w, h)
lines = connect_points(points)
for l in lines:
    l.draw(pxs)
for p in points:
    pxs[p.pos] = (255, 0, 0)

img.save("test.png", "PNG")
