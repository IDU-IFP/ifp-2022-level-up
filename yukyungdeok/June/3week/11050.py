# 11050번 이향 계수 1
a, b = list(map(int, input().split()))

up = 1
for i in range(a, a-b, -1):
    up *= i

down = 1
for i in range(1, b+1):
    down *= i

print(up // down)