import pallet_maker
import shapes
import random

def rand_squares(w, h, num, min_size, max_size):
    sqrs = []
    for i in range(num):
        center = (random.randint(0, w - 1), random.randint(0, h - 1)) # why doesnt this language have do while
        side = random.randint(min_size, max_size)
        while not valid_square(w, h, center, side):
            center = (random.randint(0, w - 1), random.randint(0, h - 1))
            side = random.randint(min_size, max_size)
        sqrs.append(shapes.Square(center, side))
    return sqrs


def valid_square(w, h, center, side):
    r = side / 2
    return 0 <= center[0] - r and center[0] + r < w and 0 <= center[1] - r and center[1] + r < h

w = 500
h = 500

img = Image.new("RGBA", (w, h), "white")
pxs = img.load()




img.save("test.png", "PNG")
