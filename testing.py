def convert_to_point(num, w, h):
    if num > 0:
        return (num if num < w else w - 1, 0 if num < w else num - w + 1)
    else:
        num *= -1
        return (0 if num < h else num - h + 1, num if num < h else h - 1)


for i in range(-18,19):
	print i, convert_to_point(i, 10, 10)
