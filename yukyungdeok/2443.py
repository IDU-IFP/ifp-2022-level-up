# 2443번 별 찍기 - 6
n = int(input())
for i in range(0,n):
    print(" " * i + "*" * (2*(n-i)-1))