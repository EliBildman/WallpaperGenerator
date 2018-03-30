import shapes
from PIL import Image


w = 5000
h = 5000
img = Image.new("RGBA", (w, h), "white")
pxs = img.load()
s = shapes.Square((2500, 2500), 5000)
s.fill(pxs, dems = (w, h), color = (0,0,255))
s.outline(pxs, dems = (w, h))
img.save("test.png", "PNG")
