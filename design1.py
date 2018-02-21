from PIL import Image
from math import sin, cos, pi

class Line(object):

    def __init__(self, ax, ay, t):
        self.ax = ax # start x
        self.ay = ay # start y
        self.t = t # theta


    def print_line(self, pxs, w, h):
        x = self.ax
        y = self.ay
        mul = 0
        while 0 <= x < w and 0 <= y <= h:
            x =

#---------------------------------------------------------------#

width = 50
height = 50

img = Image.new("RGBA", (width, height), "white")
pxs = img.load()

test = Line(10, 10, 2)
test.print_line(pxs, width, height)

img.save("test.png", "PNG")
