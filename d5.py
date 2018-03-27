import shapes
from PIL import Image


w = 50
h = 50
img = Image.new("RGBA", (w, h), "white")
pxs = img.load()
s = shapes.Square((40, 25), 20)
s.fill(pxs, dems = (w, h), color = (0,0,255))
s.outline(pxs)
print s


img.save("test.png", "PNG")
