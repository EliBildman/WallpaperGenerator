from PIL import Image
from math import sin, cos, atan, pi
from random import uniform, randint
import sys
import pallet_maker

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


def fill_colors(thetas, pxs, width, height, ax, ay, pallet):
    offset = randint(0, len(thetas) - 1)
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

                mul = (pos_in(curr_t, thetas) + offset) % len(thetas)
                pxs[x, y] = pallet[abs(len(pallet) - 1 - mul)]


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

# width = int(sys.argv[1])
# height = int(sys.argv[2])
# line_thickness = 0
# base_name = sys.argv[3]
# num_lines = randint(4, 8) * 2
# num_images = int(sys.argv[4])
# min_color_range = 50

def create_design(width, height, line_thickness, file_name, num_lines, min_color_range):
    img = Image.new("RGBA", (width, height), "white")
    pxs = img.load()

    ax = randint(width / 4,  3 * width / 4)
    ay = randint(height / 4,  3 * height / 4)

    lines = find_lines((ax, ay), (2*pi / num_lines) - 0.01, num_lines)
    thetas = []
    for l in lines:
        l.print_line(pxs, width, height, line_thickness)
        thetas.append(l.t)

    pallet = pallet_maker.spectrum_pallet(num_lines / 2 + 1, min_color_range)
    fill_colors(thetas, pxs, width, height, ax, ay, pallet)

    img.save(file_name + ".png", "PNG")
