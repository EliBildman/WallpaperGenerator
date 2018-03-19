from random import randint

def r_color():
    return tuple(randint(0, 255) for i in range(3))

def make_base(min_range):
    return tuple(randint(0, 255 - min_range) for i in range(3))

def spectrum_pallet(n, min_range = 50, base = None):
    if base == None:
        base = make_base(min_range)
    top = tuple(randint(x + min_range, 255) for x in base)
    pallet = []
    for i in range(0, n):
        pallet.append(tuple(base[j] + ((top[j] - base[j]) / n) * i for j in range(len(base))))
    return pallet

def random_pallet(n):
    pallet = []
    for i in range(n):
        pallet.append(r_color())
    return pallet

def mix_pallet(n, mix = (255, 255, 255)):
    pallet = []
    for i in range(n):
        pallet.append((randint(0, 255) + mix[0] / 2, randint(0, 255) + mix[1] / 2, randint(0, 255) + mix[2] / 2))
    return pallet
