#https://www.acmicpc.net/problem/2711
for _ in range(int(input())):
    n,w = list(input().split())
    print(w[0:int(n)-1]+w[int(n):])