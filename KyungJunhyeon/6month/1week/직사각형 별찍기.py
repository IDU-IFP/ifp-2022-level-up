a, b = map(int, input().split())
for i in range(b):
    for i in range(a):
        if i != a-1:
            print("*", end="")
        else:
            print("*")
