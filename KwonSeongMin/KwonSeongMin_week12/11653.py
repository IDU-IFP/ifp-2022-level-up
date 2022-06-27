#https://www.acmicpc.net/problem/11653

n = int(input())

for i in range(2,n):
    while n%i==0:
        print(i)
        n /= i

if n > 1:
    print(n)