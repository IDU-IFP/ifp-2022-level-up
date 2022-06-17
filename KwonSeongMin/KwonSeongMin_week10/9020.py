#https://www.acmicpc.net/problem/9020

# 처음 풀이
import math
import sys

input = sys.stdin.readline

list = [_ for _ in range(10001)]

list[0] = list[1] = 0

for i in range(2, int(math.sqrt(10000))+1):
    for j in range(i, 10001, i):
        if j != i:
            list[j] = 0

for i in range(int(input())):
    n = int(input())
    a = n//2
    b = n-a
    for i in list:
        if a in list and b in list and a + b == n:
            print(a, b)
            break
        else:
            a -= 1
            b += 1      # a와 b케이스로 나누어서 일일이 다 더하고 빼다보다 시간이 너무 오래걸림

# 두번째 풀이 
import sys
input = sys.stdin.readline

list = [1 for _ in range(10001)]

list[0] = list[1] = 0

for i in range(2, 101):
    for j in range(i, 10001, i):
        if j != i:
            list[j] = 0

for i in range(int(input())):
    n = int(input())
    for j in range(n//2, 10000):
        if list[j] and list[n-j]:
            print(n-j, j)
            break
