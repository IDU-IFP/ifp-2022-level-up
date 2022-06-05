import sys

n=int(sys.stdin.readline())
sum=0

for _ in range(n):
    p,a=map(int, sys.stdin.readline().split())

    sum=sum+(a%p)

print(sum)