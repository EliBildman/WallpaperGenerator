from PIL import Image
from math import sin, cos, pi
from random import uniform, randint

class Line(object):

    def __init__(self, ax, ay, t):
        self.ax = ax # start x
        self.ay = ay # start y
        self.t = t # theta


    def print_line(self, pxs, w, h):
        mul = 0
        while 0 <= self.ax + int(cos(self.t) * mul) < w and 0 <= self.ay + int(sin(self.t) * mul) < h:
            pxs[self.ax + int(cos(self.t) * mul), self.ay + int(sin(self.t) * mul)] = (0, 0, 0)
            mul += 1
#---------------------------------------------------------------#

width = 1920
height = 1080

img = Image.new("RGBA", (width, height), "white")
pxs = img.load()

x = randint(0, width - 1)
y = randint(0, height - 1)
ang = 0
while ang <= 2 * pi:
    ang += uniform(pi/16, pi/4)
    l = Line(x, y, ang)
    l.print_line(pxs, width, height)

img.save("test.png", "PNG")
