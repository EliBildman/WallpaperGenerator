def nums_crossed(n1, n2, nums):
    crossed = []
    for num in nums:
        if n1 < num < n2:
            crossed.append(num)
    return crossed

nums = [-1, -2, 3]
print nums_crossed(-5, 4, nums)
