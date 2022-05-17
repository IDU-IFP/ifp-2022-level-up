# 2576번 홀수

import sys
input = sys.stdin.readline
li = []
for _ in range(7):
    n = int(input())
    if n % 2 != 0: li.append(n)
if li:
    print(sum(li))
    print(min(li))
else:
    print(-1)