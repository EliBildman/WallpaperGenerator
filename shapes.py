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
            self.p1 = point_a
            self.p2 = point_b
            self.points = self.__find_points(point_a, point_b)
        else:
            self.p1 = point_b
            self.p2 = point_a
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
        if p1 not in points:
            points.insert(0, p1)
        if p2 not in points:
            points.append(p2)
        return points

    def draw(self, pxs, color = (0,0,0), thickness = 0, ignore = None):
        for point in self.points:
            for x in range(point[0] - thickness, point[0] + thickness + 1):
                for y in range(point[1] - thickness, point[1] + thickness + 1):
                    if  ignore == None or pxs[x, y] != ignore:
                        pxs[x, y] = color

    def collides_with(self, other):
        if self.p1[0] <= other.p2[0] and self.p2[0] >= other.p1[0]:
            x = self.p1[0] if self.p1[0] > other.p1[0] else other.p1[0]
            bigger_at_start = self if self[x] > other[x] else other
            x = self.p2[0] if self.p2[0] < other.p2[0] else other.p2[0]
            bigger_at_end = self if self[x] >= other[x] else other
            return bigger_at_start != bigger_at_end
        else:
            return False

    def __str__(self):
        return str(self.p1) + "-" + str(self.p2)

    def __getitem__(self, key):
        return self.p1[1] + (float(self.p2[1] - self.p1[1]) / (self.p2[0] - self.p1[0]) * (key - self.p1[0])) if self.p2[0] - self.p1[0] > 0 else self.p1[1]


class Triangle(object):

    def __init__(self, point1, point2, point3):
        self.verts = [point1, point2, point3]
        self.lines = self.__find_lines(self.verts)
        self.sorted_verts = self.__sort_pointsx(self.verts)
        self.sorted_lines = self.__find_lines(self.sorted_verts)

    def __find_lines(self, verts):
        lines = []
        for i in range(len(verts)):
            lines.append(Line_Seg(verts[i], verts[(i + 1) % 3]))
        return lines

    def __sort_pointsx(self, points):
        sorted = []
        taken = []
        for i in range(3):
            mini = None
            for j in range(len(points)):
                if (mini == None or points[j][0] < points[mini][0]) and j not in taken:
                    mini = j
            sorted.append(points[mini])
            taken.append(mini)
        return sorted

    def __extrema(self, var, ext): # var = 0: x var = 1: y, ext = 0: min ext = 1: max (sorry)
        both = [self.verts[0], self.verts[0]]
        for vert in self.verts:
            if vert[var] < both[0][var]:
                both[0] = vert
            elif vert[var] > both[1][var]:
                both[1] = vert
        return both[ext][var]

    def outline(self, pxs, color = (0,0,0)):
        for line in self.lines:
            line.draw(pxs, color = color)

    def fill(self, pxs, color, ignore = None):
        for x in range(self.__extrema(0, 0), self.__extrema(0, 1) + 1):
            for y in range(self.__extrema(1, 0), self.__extrema(1, 1) + 1):
                if self.contains_point((x, y)):
                    pxs[x, y] = color

    def contains_point(self, point):
        if self.sorted_verts[0][0] <= point[0] <= self.sorted_verts[2][0]:
            if point[0] <= self.sorted_verts[1][0]:
                return self.sorted_lines[0][point[0]] <= point[1] <= self.sorted_lines[2][point[0]] or self.sorted_lines[0][point[0]] >= point[1] >= self.sorted_lines[2][point[0]]
            else:
                return self.sorted_lines[1][point[0]] <= point[1] <= self.sorted_lines[2][point[0]] or self.sorted_lines[1][point[0]] >= point[1] >= self.sorted_lines[2][point[0]]
        return False

    def collides_with(self, other):
        for l1 in self.lines:
            for l2 in other.lines:
                if l1.collides_with(l2):
                    return True
        for vert in self.verts:
            if other.contains_point(vert):
                return True
        for vert in other.verts:
            if self.contains_point(vert):
                return True
        return False

    def __str__(self):
        return str(self.verts)

class NGon(object):

    def __init__(*args):
        self = args[0]
        self.points = args[1:] if len(args) > 2 else args[1]
        self.tris = self.__find_tris(self.points)

    def __find_tris(self, points):
        tris = []
        for i in range(2, len(points)):
            tris.append(Triangle(points[0], points[i - 1], points[i]))
        return tris

    def outline(self, pxs, color=(0,0,0)):
        self.tris[0].lines[0].draw(pxs, color)
        self.tris[-1].lines[2].draw(pxs, color)
        for tri in self.tris:
            tri.lines[1].draw(pxs, color)

    def fill(self, pxs, color, ignore = None):
        for tri in self.tris:
            tri.fill(pxs, color, ignore)

    def contains_point(self, point):
        for tri in self.tris:
            if tri.contains_point(point):
                return True
        return False

    def collides_with(self, other):
        for t1 in self.tris:
            for t2 in other.tris:
                if t1.collides_with(t2):
                    return True
        return False

    def __str__(self):
        return str(self.points)

class Rectangle(NGon):

    def __init__(self, point1, point2):
        NGon.__init__(self, point1, (point1[0], point2[1]), point2, (point2[0], point1[1]))
