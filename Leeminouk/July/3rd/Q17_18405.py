from collections import deque
import sys
input = sys.stdin.readline

# n, k = list(map(int, input().split()))
# test, graph = [], [[] for _ in range(k)]

# for x in range(n):
#     t = list(map(int, input().split()))
#     test.append(t)
#     for y, i in enumerate(t):
#         if i > 0:
#             graph[i - 1].append((x, y))

# s, X, Y = map(int, input().split())

# def bfs(test):
#     global graph
#     queue = deque()
#     queue.extend([b for a in graph for b in a])
#     temp = deque()
#     count = 0

#     while True:
#         if count == s:
#             break

#         count += 1
#         while queue:
#             x, y = queue.popleft()
#             type = test[x][y]

#             if searchFour(x - 1, y):
#                 test[x - 1][y] = type
#                 temp.append((x - 1, y))

#             if searchFour(x, y + 1):
#                 test[x][y + 1] = type
#                 temp.append((x, y + 1))

#             if searchFour(x + 1, y):
#                 test[x + 1][y] = type
#                 temp.append((x + 1, y))

#             if searchFour(x, y - 1):
#                 test[x][y - 1] = type
#                 temp.append((x, y - 1))

#         queue.extend(temp)

#     return test[X - 1][Y - 1]

# def searchFour(x, y):
#     global test
#     if x < 0 or x >= n or y < 0 or y >= n:
#         return False

#     if test[x][y] > 0:
#         return False

#     if test[x][y] == 0:
#         return True

# print(bfs(test))

n, k = list(map(int, input().split()))
test, graph = [], []

for a in range(n):
    t = list(map(int, input().split()))
    test.append(t)
    for b, i in enumerate(t):
        if i > 0:
            graph.append((i, 0, a, b))

queue = deque(sorted(graph))

S, X, Y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while queue:
    v, s, x, y = queue.popleft()

    if s == S:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if test[nx][ny] == 0:
                test[nx][ny] = v
                queue.append((v, s + 1, nx, ny))

print(test[X - 1][Y - 1])