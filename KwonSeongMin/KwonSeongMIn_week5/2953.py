#https://www.acmicpc.net/problem/2953

res = []
for _ in range(5):
    n = list(map(int,input().split()))
    res.append(sum(n))

print(res.index(max(res))+1,max(res))