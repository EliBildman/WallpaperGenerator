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

#-----------------------------------------------------------------------------------------------------------------------------------------------------#

def find_lines(center, vari, num):
    lines = []
    for x in range(num):
        lines.append(Line(center[0], center[1], ((2 * pi / num) * x) + uniform(-vari / 2, vari / 2)))
    return lines


def fill_colors(thetas, pxs, width, height, ax, ay):
    pallet = spectrum_pallet(len(thetas) / 2 + 1)
    offset = randint(0, len(pallet) - 1)
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

                mul = (pos_in(curr_t, thetas) + 1) % len(pallet)
                pxs[x, y] = pallet[abs(len(pallet) - 1 - mul)]

def spectrum_pallet(n):
    min_range = 50
    base = (randint(0, 255 - min_range), randint(0, 255 - min_range), randint(0, 255 - min_range))
    top = (randint(base[0] + min_range, 255), randint(base[1] + min_range, 255), randint(base[2] + min_range, 255))
    pallet = []
    for i in range(0, n):
        pallet.append(tuple(base[j] + ((top[j] - base[j]) / n) * i for j in range(len(base))))
    print(pallet)
    return pallet

def offset(arr, n):
    narr = []
    for i in range(n, len(arr)):
        narr.append(arr[i])
    for i in range(n):
        narr.append(arr[i])
    return narr

def pos_in(num, arr):
    for i in range(len(arr)):
        if arr[i] > num:
            return i
    return 0

#-----------------------------------------------------------------------------------------------------------------------------------------------------#

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

fill_colors(thetas, pxs, width, height, ax, ay)

img.save("filled.png", "PNG")
