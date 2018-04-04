import shapes
a = shapes.Line_Seg((0,0), (5,5))
b = shapes.Line_Seg((0,3), (5,3))
print a.collision_point(b)
