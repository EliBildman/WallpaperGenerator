from PIL import Image
from shapes import Line_Seg, Triangle

img = Image.new("RGBA", (100, 100), "white")
pxs = img.load()

# t = Triangle((20, 20), (21, 70), (70, 50))
# t.outline(pxs, (0, 0, 0))

l = Line_Seg((10, 10), (30, 50))
l.draw(pxs, (0, 0, 0))

img.save("test.png", "PNG")
