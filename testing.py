def func1(x):
    return x*2

def func2(z, y = func1(z)):
    return y

print func2(2)
