from PIL import Image

width = 40
height = 20

img = Image.new("RGBA", (width, height), "white")
pxs = img.load()

pxs[10, 10] = (255, 0, 0)

img.save("test.png", "PNG")
print "Done"
