from random import randint

def make_base(min_range):
    return tuple(randint(0, 255 - min_range) for i in range(3))

def spectrum_pallet(n, min_range, base = None):
    if base == None:
        base = make_base(min_range)
    top = tuple(randint(x + min_range, 255) for x in base)
    pallet = []
    for i in range(0, n):
        pallet.append(tuple(base[j] + ((top[j] - base[j]) / n) * i for j in range(len(base))))
    return pallet
