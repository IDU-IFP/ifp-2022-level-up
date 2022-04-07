from tkinter import N


x, y = map(int, input().split())

def gcb(x, y):
    while y > 0:
        x, y = y, x % y

    return x

def lcm(x, y):
    return x * y // gcb(x, y)

print(gcb(x, y))
print(lcm(x, y))