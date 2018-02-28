from PIL import Image
from shapes import Line_Seg

img = Image.new("RGBA", (100, 100), "white")
pxs = img.load()

l = Line_Seg((10, 10), (20, 20))
l.draw(pxs, (0, 0, 0))

img.save("test.png", "PNG")
