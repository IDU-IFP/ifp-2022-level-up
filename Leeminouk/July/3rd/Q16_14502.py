from itertools import combinations
import sys
input = sys.stdin.readline

def dfs(graph, x, y):
    n, m = len(graph), len(graph[0])

    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 2

        dfs(graph, x - 1, y)
        dfs(graph, x + 1, y)
        dfs(graph, x, y - 1)
        dfs(graph, x, y + 1)
        return graph

    return graph

n, m = map(int, input().split())
graph, total, virus, empty = [], [], [], []

for i in range(n):
    t = list(map(int, input().split()))
    graph.append(t)

    for j, h in enumerate(t):
        if h == 0:
            empty.append((i, j))
        
        if h == 2:
            virus.append((i, j))

empty_space = list(combinations(empty, 3))

for set in empty_space:
    temp_graph = []
    for i in graph:
        temp_graph.append(i.copy())

    for x, y in set:
        temp_graph[x][y] = 1
    
    for x, y in virus:
        temp_graph[x][y] = 0
        result = dfs(temp_graph, x, y)
        temp_graph = result

    t = 0
    for a in result:
        t += a.count(0)
    total.append(t)

print(max(total))

# 이것이 코딩 테스트다 답안지. 시간 초과됨..

# n, m = map(int, input().split())
# data = []
# temp = [[0] * m for _ in range(n)]

# for i in range(n):
#     data.append(list(map(int, input().split())))

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# result = 0

# def virus(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if nx >= 0 and nx < n and ny >= 0 and ny < m:
#             if temp[nx][ny] == 0:
#                 temp[nx][ny] = 2
#                 virus(nx, ny)

# def get_score():
#     score = 0
#     for i in temp:
#         score += i.count(0)

#     return score

# def dfs(count):
#     global result

#     if count == 3:
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j] = data[i][j]

#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j] == 2:
#                     virus(i, j)

#         result = max(result, get_score())
#         return

#     for i in range(n):
#         for j in range(m):
#             if data[i][j] == 0:
#                 data[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 data[i][j] = 0
#                 count -= 1

# dfs(0)
# print(result)