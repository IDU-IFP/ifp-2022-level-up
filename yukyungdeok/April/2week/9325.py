# 9325번 얼마?
n = int(input())

for i in range(n):
    a = int(input())
    b = int(input())
    
    for j in range(b):
        x,y = map(int, input().split())
        a += x * y
    print(a)