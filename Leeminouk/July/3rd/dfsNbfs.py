from collections import deque

def dfs(v, visited):
    global graph
    visited[v] = True

    print(v, end=" ")

    for a in graph[v]:
        if not visited[a]:
            dfs(a, visited)

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = []

while True:
    t = input()
    if t == "-1":
        break

    else:
        if t == "0":
            graph.append([])    
        else:
            graph.append(list(map(int, t.split())))

visited = [False] * len(graph)

bfs(graph, 1, visited)
# dfs(1, visited)