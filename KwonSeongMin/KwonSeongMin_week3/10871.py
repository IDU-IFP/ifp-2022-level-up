#https://www.acmicpc.net/problem/10871

n, x = map(int, input().split())
num = list(map(int, input().split()))
for i in range(n):
    if num[i] < x:
        print(num[i])