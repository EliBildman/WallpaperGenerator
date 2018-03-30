import shapes

sqr = shapes.Square((10,10), 1237012)
w = 50
h = 50
print 0 > sqr.center[0] - sqr.r and w <= sqr.center[0] + sqr.r and 0 >= sqr.center[1] - sqr.r and h <= sqr.center[1] + sqr.r
