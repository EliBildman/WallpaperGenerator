from PIL import Image
from math import sin, cos, atan, pi
from random import uniform, randint

class Line(object):

    def __init__(self, ax, ay, t):
        self.ax = ax # start x
        self.ay = ay # start y
        self.t = t # theta

    def print_line(self, pxs, w, h, thickness):
        mul = 0
        while 0 <= self.ax + int(cos(self.t) * mul) < w and 0 <= self.ay + int(sin(self.t) * mul) < h:
            xpos = self.ax + int(cos(self.t) * mul)
            ypos = self.ay + int(sin(self.t) * mul)
            for x in range(xpos - thickness, xpos + thickness):
                for y in range(ypos - thickness, ypos + thickness):
                    if 0 <= x < w and 0 <= y < h:
                        pxs[x, y] = (0, 0, 0)
            mul += 1

#---------------------------------------------------------------#

def find_lines(center, minDt, maxDt):
    ang = uniform(minDt, maxDt / 2)
    lines = []
    while ang <= 2 * pi:
        lines.append(Line(center[0], center[1], ang))
        ang += uniform(minDt, maxDt)
    return lines

def fill_colors(thetas, pxs, width, height, ax, ay):
    for x in range(width):
        for y in range(height):
            rx = x - ax
            ry = y - ay
            if pxs[x, y] == (255, 255, 255, 255):
                if rx != 0:
                    curr_t = atan(float(ry) / rx) + (pi if rx < 0 else 0)
                    if curr_t < 0:
                        curr_t += 2 * pi
                else:
                    curr_t = (pi/2) if ry > 0 else (3 * pi/2)

                mul = pos_in(curr_t, thetas) + 1
                #print(rx, ry, curr_t)
                pxs[x, y] = (10 * mul, 30 * mul, 50 * mul)


def pos_in(num, arr):
    for i in range(len(arr)):
        if arr[i] > num:
            return i
    return 0

width = 1920
height = 1080

img = Image.new("RGBA", (width, height), "white")
pxs = img.load()

ax = randint(0, width - 1)
ay = randint(0, height - 1)

lines = find_lines((ax, ay), pi/16, pi/2)
thetas = []
for l in lines:
    l.print_line(pxs, width, height, 2)
    thetas.append(l.t)

#print(thetas)

img.save("skeleton.png", "PNG")

fill_colors(thetas, pxs, width, height, ax, ay)

img.save("filled.png", "PNG")
