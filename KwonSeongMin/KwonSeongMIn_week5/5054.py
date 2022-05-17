#https://www.acmicpc.net/problem/5054

for _ in range(int(input())):
    t = int(input())
    n = list(map(int,input().split()))
    print((max(n)*2)-(min(n)*2))