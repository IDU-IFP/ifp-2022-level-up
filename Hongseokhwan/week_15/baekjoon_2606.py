# 바이러스

def dfs(graph, v, visited): # dfs 알고리즘
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)

com = int(input()) # 컴퓨터 수
ssang = int(input()) # 연결된 쌍의 수
count = 0 # 감엄된 컴퓨터 개수

graph = [[] for i in range(com+1)] # 컴퓨터별 연결된 컴퓨터를 담을 집합
visited = [False for i in range(com+1)] # 컴퓨터별 감염 여부

for i in range(ssang): # 컴퓨터별 연결된 컴퓨터 정리
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, 1, visited) # 컴퓨터 감염 여부 확인

for i in visited: # True 인 경우 감염이므로 카운트
    if (i == True):
        count += 1

print(count - 1) # 1번 컴퓨터를 제외한 감염 컴퓨터 개수 출력