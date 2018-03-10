from shapes import NGon
from random import randint
from PIL import Image
from pallet_maker import spectrum_pallet

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
        if n1 <= num <= n2:
            crossed.append(num)
    return crossed

def generate_tris(num, w, h):
    shapes = []
    corners = [-1 * h + 1, 0, w - 1, w + h - 2]
    x = randint(w/3, 2 * w/3)
    y = randint(h/3, 2 * h/3)
    nums = find_nums(num, w, h)
    for i in range(num):
        if nums[i] < nums[(i+1) % num]:
            cors_crossed = nums_crossed(nums[i], nums[(i+1) % num], corners)
        else:
            cors_crossed = nums_crossed(nums[i], w + h - 2, corners) + nums_crossed(-w - h + 2, nums[(i+1) % num], corners)
        if len(cors_crossed) > 0:
            verts = [(x,y), convert_to_point(nums[i], w, h), convert_to_point(nums[(i+1) % num], w, h)]
            for cor in cors_crossed[::-1]:
                verts.insert(2, convert_to_point(cor, w, h))
            shapes.append(NGon(verts))
        else:
            shapes.append(NGon((x,y), convert_to_point(nums[i], w, h), convert_to_point(nums[(i+1) % num], w, h)))
    return shapes

w = 1920
h = 1080
n = 8
offset = randint(0, n-1)
img = Image.new("RGBA", (w, h), "blue")
pxs = img.load()
tris = generate_tris(n, w, h)
pallet = spectrum_pallet(n/2 + 1, 50)
for i in range(len(tris)):
    print "Filling tri", i+1
    tris[i].fill(pxs, pallet[abs(n/2 - (((i+offset)%n) + 1))])
pxs[w-1,h-1] = (0,0,0)
img.save("test.png", "PNG")
