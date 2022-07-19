# DFS와 BFS

from collections import deque

def dfs(graph, v, visited): # dfs 알고리즘
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            visited[v] = True
            dfs(graph, i, visited)

def bfs(graph, start, visited): # bfs 알고리즘
    d = deque([start])
    visited[start] = True

    while d:
        e = d.popleft()
        print(e, end=" ")

        for i in graph[e]:
            if not visited[i]:
                visited[i] = True
                d.append(i)

n, m ,v = map(int, input().split()) # 정점, 간선, 시작할 정점의 번호 입력
graph = [[] for i in range(n+1)] # 정점별 연결된 정점의 집합
dfs_visited = [False for i in range(n+1)] # dfs 알고리즘 정점 방문 체크
bfs_visited = [False for i in range(n+1)] # bfs 알고리즘 정점 방문 체크

for i in range(m): # 정점별 연결된 정점들을 정리
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

for i in graph: # 정점 번호를 오름차순으로 정렬
    i.sort()

dfs(graph, v, dfs_visited) # dfs 출력
print()
bfs(graph, v, bfs_visited) # bfs 출력