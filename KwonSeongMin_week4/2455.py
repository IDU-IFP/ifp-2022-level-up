#https://www.acmicpc.net/problem/2455
#지능형 기차
m,n=0,0
for _ in range(4):
    o,i = map(int,input().split())
    n-=o
    n+=i
    if n > m:
        m = n
print(m)