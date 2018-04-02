import shapes
from PIL import Image


w = 100
h = 100
img = Image.new("RGBA", (w, h), "white")
pxs = img.load()
s = shapes.Square((50, 50), 20)
s.fill(pxs, dems = (w, h), color = (0,0,255))
s.outline(pxs, dems = (w, h))
print s
img.save("test.png", "PNG")
