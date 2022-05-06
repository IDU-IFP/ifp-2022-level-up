n, m = map(int, input().split())

array = [[(n, m) for m in range(1, m+1)]for n in range(1, n+1)]

for arr in array:
    for a in arr:
        print(*a)
