import sys
input = sys.stdin.readline

A = int(input())

for _ in range(A):
    B = int(input())
    print(sum(list(map(int, input().split()))))