import sys
input = sys.stdin.readline

def bigNumberOld():
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    n_mo = arr.pop(arr.index(max(arr)))
    n_mt = arr.pop(arr.index(max(arr)))

    count = 1
    total = 0
    for _ in range(m):
        if count > k:
            count = 1
            total += n_mt
        else:
            total += n_mo

        count += 1

    return total

def bigNumberNew():
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    n_mo = arr.pop(arr.index(max(arr)))
    n_mt = arr.pop(arr.index(max(arr)))

    d = int(m / k)
    t_one = (m - d) * n_mo
    t_sec = d * n_mt

    return t_one + t_sec

# print(bigNumberNew())

# def numCardOld():
    