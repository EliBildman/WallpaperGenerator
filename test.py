def offset(arr, n):
    narr = []
    for i in range(n, len(arr)):
        narr.append(arr[i])
    for i in range(n):
        narr.append(arr[i])
    return narr

arr = [0, 1, 2, 3, 4]
print offset(arr, 6)
