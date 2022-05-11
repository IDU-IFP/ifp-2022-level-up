#https://www.acmicpc.net/problem/1427

n = list(input())
n.sort(reverse=True)
for res in n:
    print(res,end='')