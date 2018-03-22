import random

def comb_randint(*args):
    pos = []
    for r in args:
        pos += range(r[0], r[1] + 1)
    return random.choice(pos)

def most_square(num):
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            l = i
    return (l, num / l)

def to_hsv(rgb):
    None

def to_rgb(hsv):
    h = hsv[0]
    c = hsv[1] * hsv[2]
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = hsv[2] - c
    print c, x, m
    rgb = ()
    if h < 60:
        rgb = (c, x, 0)
    elif h < 120:
        rgb = (x, c, 0)
    elif h < 180:
        rgb = (0, c, x)
    elif h < 240:
        rgb = (0, x, c)
    elif h < 300:
        rgb = (x, 0, c)
    else:
        rgb = (c, 0, x)
    rgb = tuple((rgb[i] + m) * 255 for i in range(3))
    return rgb
