import numpy as np
n = int(input())
result = np.zeros((19, 19), dtype=int)
for _ in range(n):
    x, y = map(lambda num: int(num)-1, input().split())
    result[x][y] = 1

for i in result:
    print(i)
