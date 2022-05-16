# 2506번 점수계산

n = int(input())
li = list(map(int, input().split()))
x = 0
y = 0

for i in range(n):
    if li[i] == 0:
        y = 0
    else:
        y += 1
        x += y
print(x)