from math import sin, cos, atan, pi

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
        if point_a[0] < point_b[0]:
            self.points = self.__find_points(point_a, point_b)
        else:
            self.points = self.__find_points(point_b, point_a)


    def __find_points(self, p1, p2):
        points = []
        t = atan((float(p2[1]) - p1[1]) / (p2[0] - p1[0])) if p2[0] > p1[0] else (pi/2 if p2[1] > p1[1] else -1 * pi/2)
        x = float(p1[0])
        y = float(p1[1])
        while x < p2[0] or (p2[1] >= p1[1] and y < p2[1]) or (p2[1] < p1[1] and y > p2[1]):
            points.append((int(x), int(y)))
            x += cos(t)
            y += sin(t)
        return points

    def draw(self, pxs, color, ignore = None):
        for point in self.points:
            if ignore == None or pxs[point[0], point[1]] != ignore:
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
        self.lines = self.__find_lines(self.verts)

    def __find_lines(self, verts):
        lines = []
        for i in range(len(verts)):
            lines.append(Line_Seg(verts[i], verts[(i + 1) % 3]))
        return lines

    def outline(self, pxs, color):
        for i in range(len(self.verts)):
            Line_Seg(self.verts[i], self.verts[(i + 1) % 3]).draw(pxs, color)

    def fill(self, pxs, color, ignore = None):
        for i in range(len(self.verts)):
            for point in self.lines[(i + 1) % len(self.lines)].points[1: -1]:
                Line_Seg(self.verts[i], point).draw(pxs, color, ignore)

class NGon(object):

    def __init__(self, points):
        #points = array of tuple points format (x, y) given in the order theyre connected
        self.points = points
        self.tris = self.__find_tris(points)

    def __find_tris(self, points):
        tris = []
        for i in range(2, len(points)):
            tris.append(Triangle(points[0], points[i - 1], points[i]))
        return tris

    def outline(self, pxs, color):
        self.tris[0].lines[0].draw(pxs, color)
        self.tris[-1].lines[2].draw(pxs, color)
        for tri in self.tris:
            tri.lines[1].draw(pxs, color)

    def fill(self, pxs, color, ignore = None):
        for tri in self.tris:
            tri.fill(pxs, color, ignore)
