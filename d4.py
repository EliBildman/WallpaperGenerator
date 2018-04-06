from shapes import Point, Line_Seg
from random import randint
from PIL import Image
import helpers
import pallet_maker

def random_points(w, h, avg_dis, variance):
    points = []
    for x in range(0, w, avg_dis):
        for y in range(0, h, avg_dis):
            ix = x + randint(-variance, variance)
            iy = y + randint(-variance, variance)
            if 0 <= ix < w and 0 <= iy < h:
                points.append(shapes.Point(ix , iy))
    return points

def find_nums(n, w, h):
    nums = []
    for i in range(n):
        mul = (2*(w+h) - 1) / n
        nums.append(randint(mul * i, mul * (i+1)) - (w + h))
    return nums

def convert_to_point(num, w, h):
    if num > 0:
        return (num if num < w else w - 1, 0 if num < w else num - w + 1)
    else:
        num *= -1
        return (0 if num < h else num - h + 1, num if num < h else h - 1)

def random_edge_points(n, w, h):
    points = find_nums(n, w, h)
    for i in range(len(points)):
        points[i] = convert_to_point(points[i], w, h)
    return points

def r_sym_edge_points(w, h):
    max = 6
    points = [(0,0), (0,h-1), (w-1, h-1), (w-1,0)]
    # hor = randint(1, int(float(w) / (w + h) * 10))
    # ver = randint(1, int(float(h) / (w + h) * 10))
    hor = 2
    ver = 1
    # hor = 1
    # ver = 12
    for i in range(1, hor + 1):
        points += [(w / (hor + 1) * i, 0), (w / (hor + 1) * i, h - 1)]
    for i in range(1, ver + 1):
        points += [(0, h / (ver + 1) * i), (w - 1, h / (ver + 1) * i)]
    return points

def connect_points(points):
    lines = []
    for j in range(len(points)):
        point = points[j]
        for i in range(2 - len(point.lines)):
            o_ind = randint(0, len(points) - 1)
            while (o_ind == j) or (points[o_ind] in point.lines) or (any_collisions(shapes.Line_Seg(point.pos, points[o_ind].pos), lines)):
                o_ind = randint(0, len(points) - 1)
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



w = 1000
h = 500

img = Image.new("RGBA", (w, h), "white")
pxs = img.load()

points = r_sym_edge_points(w, h)
# lines = connect_points(points)
# for l in lines:
#     l.draw(pxs, thickness = 2)
lines = []
for i in range(len(points)):
    for j in range(i, len(points)):
        lines.append(Line_Seg(points[i], points[j]))
        lines[-1].draw(pxs)
# cols = []
# for i in range(len(lines)):
#     for j in range(i, len(lines)):
#         c = lines[i].collision_point(lines[j])
#         if c != None:
#             cols.append((int(c[0]), int(c[1])))
# for c in cols:
#     pxs[c] = (255, 0, 0)
n = 10
pallet = pallet_maker.mix_pallet(n)
for x in range(w):
    for y in range(h):
        if pxs[x, y] != (0,0,0,255):
            pxs[x,y] = pallet[helpers.lines_crossed(lines, (x, 0), (x, y)) % n]
    print x


#print cols

img.save("test.png", "PNG")
