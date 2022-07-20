import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
way, result = [[] for _ in range(n + 1)], [-1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    way[a].append(b)

road = deque([x])
result[x] = 0
while road:
    pos = road.popleft()
    for i in way[pos]:
        if result[i] == -1:
            result[i] = result[pos] + 1
            road.append(i)

check = False
for i in range(1, n + 1):
    if result[i] == k:
        print(i)
        check = True

if not check:
    print(-1)