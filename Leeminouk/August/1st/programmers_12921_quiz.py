def solution(n):
    return prime(n)

def prime(n):
    t = [True] * (n + 1)
    t[0], t[1] = False, False
    h = int(n ** .5)

    for i in range(2, h + 1):
        for j in range(i * i, n + 1, i):
            t[j] = False

    return t.count(True)

print(solution(int(input())))