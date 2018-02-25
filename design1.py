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

def find_lines(center, vari, num):
    lines = []
    for x in range(num):
        lines.append(Line(center[0], center[1], ((2 * pi / num) * x) + uniform(-vari / 2, vari / 2)))
    return lines


def fill_colors(thetas, pxs, width, height, ax, ay):
    pallet = spectrum_pallet(len(thetas))
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
                mul = pos_in(curr_t, thetas)
                pxs[x, y] = pallet[mul]

def spectrum_pallet(n):
    base = (randint(0, 255), randint(0, 255/n), randint(0, 255/n))
    top = (randint(base[0], 255), randint(base[1], 255), randint(base[2], 255))
    pallet = []
    for i in range(1, n + 1):
        pallet.append(tuple( for x in base))
    return pallet

def pos_in(num, arr):
    for i in range(len(arr)):
        if arr[i] > num:
            return i
    return 0

width = 1920
height = 1080

img = Image.new("RGBA", (width, height), "white")
pxs = img.load()

ax = randint(width / 4,  3 * width / 4)
ay = randint(height / 4,  3 * height / 4)

lines = find_lines((ax, ay), pi/4, 6)
thetas = []
for l in lines:
    l.print_line(pxs, width, height, 0)
    thetas.append(l.t)

#print(thetas)

img.save("skeleton.png", "PNG")

fill_colors(thetas, pxs, width, height, ax, ay)

img.save("filled.png", "PNG")
