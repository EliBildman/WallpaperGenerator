from shapes import NGon
from random import randint
from PIL import Image

def find_nums(n, w, h):
    nums = []
    for i in range(n):
        mul = (2*(w+h) - 1) / n
        nums.append(randint(mul * i, mul * (i+1)) - (w + h))
    return nums

def convert_to_point(num, w, h):
    if num > 0:
        return (num if num < w else w - 1, 0 if num < w else num - w + 1)
    else:
        num *= -1
        return (0 if num < h else num - h + 1, num if num < h else h - 1)

def nums_crossed(n1, n2, nums):
    crossed = []
    for num in nums:
        if abs(n1) < abs(num) < abs(n2):
            crossed.append(num)
    return crossed

def generate_tris(num, w, h):
    shapes = []
    x = w/2
    y = h/2
    corners = [-1 * h + 1, 0, w - 1]
    # x = randint(0, w - 2)
    # y = randint(0, h - 1)
    #nums = find_nums(num, w, h)
    nums = [5, 750]
    for i in range(num):
        cors_crossed = nums_crossed(nums[i], nums[(i+1) % num], corners)
        if len(cors_crossed) > 0:
            verts = [(x,y), convert_to_point(nums[i], w, h), convert_to_point(nums[(i+1) % num], w, h)]
            for cor in cors_crossed:
                verts.insert(2, convert_to_point(cor, w, h))
            shapes.append(NGon(verts))
        else:
            shapes.append(NGon((x,y), convert_to_point(nums[i], w, h), convert_to_point(nums[(i+1) % num], w, h)))
    return shapes

w = 500
h = 500
img = Image.new("RGBA", (w, h), "white")
pxs = img.load()
for t in generate_tris(1, w, h):
    t.outline(pxs)
img.save("test.png", "PNG")
