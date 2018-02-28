from math import sin, cos, atan

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

class Line_Seg(object):

    def __init__(self, point_a, point_b):
        self.points = self.__find_points(point_a, point_b)


    def __find_points(self, p1, p2):
        points = []
        x = p1[0]
        y = p1[1]
        


    def draw(self, pxs, color):
        for point in self.points:
            pxs[point[0], point[1]] = color


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

class Triangle(object):

    def __init__(self, point1, point2, point3):
        self.verts = [point1, point2, point3]

    def outline(self, pxs, color):
        for i in range(len(self.verts)):
            Line_Seg(self.verts[i], self.verts[(i + 1) % 3]).draw(pxs, color)

    def fill(self, pxs, color):
        for point in Line(self.verts[1], self.verts[2]):
            Line_Seg(self.verts[0], point).draw(pxs, color)

class NGon(object):

    def __init__(self, points):
        #points = array of tuple points format (x, y) given in the order theyre connected
        self.points = points

    def outline(self, color):
        None

    def fill(self, color):
        None
