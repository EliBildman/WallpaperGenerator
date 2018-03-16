from PIL import Image
import pallet_maker
import shapes
import random

def rand_squares(w, h, num, min_size, max_size):
    sqrs = []
    for i in range(num):
        center = (random.randint(min_size, w - min_size - 1), random.randint(min_size, h - min_size - 1)) # why doesnt this language have do while
        side = random.randint(min_size, max_size)
        while not valid_square(w, h, center, side):
            side = random.randint(min_size, max_size)
        sqrs.append(shapes.Square(center, side))
    return sqrs

def num_contains(point, shapes):
    num = 0
    for shape in shapes:
        if shape.contains_point(point):
            num += 1
    return num

def valid_square(w, h, center, side):
    r = side / 2
    return 0 <= center[0] - r and center[0] + r < w and 0 <= center[1] - r and center[1] + r < h

w = 1920
h = 1080

img = Image.new("RGBA", (w, h), "black")
pxs = img.load()

sqrs = rand_squares(w, h, 100, w / 10, w / 3)
j = 0
for sqr in sqrs:
    j += 1
    print j
    for x in range(sqr.points[2][0], sqr.points[0][0]):
        for y in range(sqr.points[2][1], sqr.points[0][1]):
            pxs[x, y] = tuple(pxs[x,y][i] + 10 for i in range(3))

img.save("test.png", "PNG")
