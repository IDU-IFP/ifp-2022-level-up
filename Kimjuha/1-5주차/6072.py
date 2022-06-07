n = int(input())
number = list(map(int, input(), split()))


def goto(number, n, i):
    if i == n:
        return
    print(number[i])
    i += 1
    goto(number, n, i)


goto(number, n, 0)
