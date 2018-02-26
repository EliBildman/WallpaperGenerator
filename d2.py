from PIL import Image
from random import randint

class Rectangle(object):

    def __init__(self, point1, point2):
        self.ax = point1[0] #lower left
        self.ay = point1[1]
        self.bx = point2[0] #upper right
        self.by = point2[1]

    def collides_with(self, other):
        return (self.ax <= other.ax <= self.bx or other.ax <= self.ax <= other.bx) and (self.ay <= other.ay <= self.by or other.ay <= self.ay <= other.by)

    def contains_point(self, point):
        return self.ax <= point[0] <= self.bx and self.ay <= point[1] <= self.by

    def print_rec(self, pxs, color):
        for x in range(self.bx - self.ax + 1):
            pxs[self.ax + x, self.ay] = color
            pxs[self.ax + x, self.by] = color
        for y in range(self.by - self.ay + 1):
            pxs[self.ax, self.ay + y] = color
            pxs[self.bx, self.ay + y] = color


def rand_rec(w, h):
    x1 = randint(0, w - 3)
    y1 = randint(0, h - 3)
    return Rectangle((x1, y1), (randint(x1 + 2, w - 1), randint(y1 + 2, h - 1)))

def conflicts(recs, new):
    for r in recs:
        if new.collides_with(r):
            return True
    return False

def empty_spot_exists(pxs, w, h, recs):
    for x in range()
    for r in recs:

def find_recs(pxs, w, h):
    recs = []
    for x in range(100):
        tRc = rand_rec(w, h)
        while(conflicts(recs, tRc)):
            tRc = rand_rec(w, h)
        recs.append(tRc)
    return recs



width = 100
height = 100

img = Image.new("RGBA", (width, height), "white")
pxs = img.load()

for r in find_recs(pxs, width, height):
    r.print_rec(pxs, (0, 0, 0))


img.save("test.png", "PNG")
