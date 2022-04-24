# 2010번 플러그

import sys
n = int(sys.stdin.readline())
sum = 0
for _ in range(n):
    sum += int(sys.stdin.readline())
print(sum - (n - 1))