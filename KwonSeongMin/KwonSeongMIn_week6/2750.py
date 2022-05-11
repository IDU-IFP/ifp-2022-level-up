#https://www.acmicpc.net/problem/2750

n = int(input())

res = [0 for _ in range(n)] # res list를 n개의 0으로 초기화

for i in range(n):
    q = int(input())
    res[i] = q  #대입
    
res.sort()

for ans in res:
    print(ans)