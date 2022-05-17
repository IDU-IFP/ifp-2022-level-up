# 9076번 점수 집계
for _ in range(int(input())):
    n = list(map(int, input().split()))
    n.remove(max(n))
    n.remove(min(n))
    if max(n) - min(n) >= 4:
        print('KIN')
    else:
        print(sum(n))
