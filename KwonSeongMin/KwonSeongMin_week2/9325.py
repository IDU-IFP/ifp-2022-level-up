#https://www.acmicpc.net/problem/9325

for _ in range(int(input())):
    car = int(input())
    for _ in range(int(input())):
        a,b = map(int,input().split())
        car += a * b
    print(car)