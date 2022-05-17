#https://www.acmicpc.net/problem/10984

for i in range(int(input())):
    c,d = 0,0
    for j in range(int(input())):
        a,b = map(float,input().split())
        c += a
        d += a * b
    print("%d %.1f"%(c,d/c))