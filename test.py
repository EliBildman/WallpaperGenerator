from PIL import Image
import shapes
from random import randint
import math
import pallet_maker
import helpers

w = 100
h = 100

a = shapes.Line_Seg((0,1), (100,99))
b = shapes.Line_Seg((0,99), (100,1))
c = shapes.Line_Seg((0,21), (100,79))
d = shapes.Line_Seg((0,79), (100,21))

# img = Image.new("RGBA", (w, h), "white")
# pxs = img.load()
# a.draw(pxs, dems = (w, h), thickness = 1)
# b.draw(pxs, dems = (w, h), thickness = 1)
# c = a.collision_point(b)
# if c != None:
#     print "yes"
#     pxs[c] = (255,0,0)
# img.save("test.png", "PNG")

print a.collision_point(b)
print c.collision_point(d)
