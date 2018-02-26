from PIL import Image
from random import randint

class Rectangle(object):

    def __init__(self, origin, width, height):
        self.ax = origin[0] #lower left corner
        self.ay = origin[1]
        self.width = width
        self.height = height

    def collides_with(self, other):
        return (0 < self.ax - other.ax < other.width and 0 < self.ay - other.ay < other.height) or (0 < other.ax - self.ax < self.width and 0 < other.ay - self.ay < self.height)

    def contains_point(self, point):
        return self.ax <= point[0] < self.ax + width and self.ay <= point[1] < self.ay + height

    def print_rec(self, pxs):
        for x in range(self.width):
            pxs[self.ax + x, self.ay] = (0, 0, 0)
            pxs[self.ax + x, self.ay + self.height - 1] = (0, 0, 0)
        for y in range(self.height):
            pxs[self.ax, self.ay + y] = (0, 0, 0)
            pxs[self.ax + self.width - 1, self.ay + y] = (0, 0, 0)


def find_squares(pxs, w, h):
    x = randint(0, w - 3)
    y = randint(0, h - 3)
    sWid = randint(3, w - x - 1)
    sHie = randint(3, h - y - 1)
    squares = []



width = 100
height = 100

img = Image.new("RGBA", (width, height), "white")
pxs = img.load()

rec1 = Rectangle((50, 50), 20, 20)
rec2 = Rectangle((20, 20), 30, 30)

rec1.print_rec(pxs)
rec2.print_rec(pxs)
img.save("test.png", "PNG")
