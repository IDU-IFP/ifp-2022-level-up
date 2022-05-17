#https://www.acmicpc.net/problem/2693

for _ in range(int(input())):
    n = sorted(list(map(int,input().split())))
    print(n[-3])