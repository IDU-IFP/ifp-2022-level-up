from collections import deque
import sys
input = sys.stdin.readline

# frozen drink
def startFrozen():
    n, m = map(int, input().split())

    graph = []
    for _ in range(n):
        graph.append([int(a) for a in input() if a != "\n"])

    result = 0
    for i in range(n):
        for j in range(m):
            if dfsSpace(graph, i, j):
                result += 1

    return result

def dfsSpace(graph, x, y):
    if x <= -1 or x >= len(graph) or y <= -1 or y >= len(graph[0]):
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfsSpace(graph, x - 1, y)
        dfsSpace(graph, x + 1, y)
        dfsSpace(graph, x, y + 1)
        dfsSpace(graph, x, y - 1)
        return True

    return False

# print(startFrozen())

# escape maze
def startMazeEsc():
    n, m = map(int, input().split())

    graph = []
    for _ in range(n):
        graph.append([int(a) for a in input() if a != "\n"])

    return dfsMaze(graph, 0, 0)

def dfsMaze(graph, x, y):
    n, m = len(graph), len(graph[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]

print(startMazeEsc())