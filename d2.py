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

#-----------------------------------------------------------------------------------------------------------------------------------------------------#

def rand_rec(*args):
    w = args[0]
    h = args[1]
    if len(args) == 2:
        x1 = randint(0, w - 1)
        y1 = randint(0, h - 1)
        return Rectangle((x1, y1), (randint(x1, w - 1), randint(y1, h - 1)))
    elif len(args) == 3:
        spot = args[2][randint(0, len(args[2]) - 1)]
        return Rectangle(spot, (randint(spot[0], w - 1), randint(spot[1], h - 1)))

def conflicts(recs, new):
    for r in recs:
        if new.collides_with(r):
            return True
    return False

def empty_spots(pxs, w, h, recs):
    spots = []
    for x in range(w):
        for y in range(h):
            if not point_covered((x, y), recs):
                spots.append((x, y))
    return spots

def point_covered(point, recs):
    for r in recs:
        if r.contains_point(point):
            return True
    return False

def find_recs(pxs, w, h):
    recs = []
    eSpots = empty_spots(pxs, w, h, recs)
    while len(eSpots) > 0:
        #print "making rectangle " + str(len(recs))
        tRc = rand_rec(w, h, eSpots)
        while conflicts(recs, tRc):
            tRc = rand_rec(w, h, eSpots)
        recs.append(tRc)
        eSpots = empty_spots(pxs, w, h, recs)
    return recs



width = 50
height = 50

img = Image.new("RGBA", (width, height), "white")
pxs = img.load()

for r in find_recs(pxs, width, height):
    r.print_rec(pxs, (0, 0, 0))


img.save("test.png", "PNG")
