# 10883번 사과
n = int(input())
a = 0
for i in range(n):
    x,y = map(int, input().split())
    a += y % x
    print(a)