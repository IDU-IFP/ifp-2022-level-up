#https: // www.acmicpc.net/problem/15552
import sys
input = sys.stdin.readline
count = int(input())

for i in range(count):
    a, b = map(int, input().split())
    print(a+b)
