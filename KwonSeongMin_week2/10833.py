#https://www.acmicpc.net/problem/10833
c = 0
for i in range(int(input())):
    a,b = map(int,input().split())
    c += b%a
print(c)