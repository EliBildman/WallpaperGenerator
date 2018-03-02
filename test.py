from PIL import Image
from shapes import Line_Seg, Triangle, NGon
from random import randint

w = 1000
h = 1000
img = Image.new("RGBA", (w, h), "white")
pxs = img.load()

lucas = NGon([(312, 250), (750, 250), (900, 500), (750, 750), (250, 750)])

#lucas.outline(pxs, (0, 0, 0))
#img.save("outlined.png", "PNG")
lucas.fill(pxs, (0, 0, 255), (0, 0, 0, 255))
img.save("filled.png", "PNG")
