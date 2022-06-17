#https://www.acmicpc.net/problem/1929

import math
a, b = map(int, input().split())

list = [1 for _ in range(b+1)]

list[0] = list[1] = 0

for i in range(2, int(math.sqrt(b))+1):
    for j in range(i, b+1, i):
        if j != i:
            list[j] = 0
res = 0
for i in list:
    if i and res >= a:
        print(res)
    res += 1
