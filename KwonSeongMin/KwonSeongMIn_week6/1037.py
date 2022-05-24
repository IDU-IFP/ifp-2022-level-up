#https://www.acmicpc.net/problem/1037

n = int(input())
x = list(map(int, input().split()))

print(max(x) * min(x))
