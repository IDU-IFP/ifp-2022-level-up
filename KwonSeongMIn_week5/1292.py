#https://www.acmicpc.net/problem/1292

a,b = map(int,input().split())

num1,num2 = 0,0
r1,r2 = 1,1
c1,c2 = 0,0

for i in range(b):
    num1 += r1
    c1 += 1
    if r1 == c1:
        r1 += 1
        c1 = 0

for i in range(a-1):
    num2 += r2
    c2 += 1
    if r2 == c2:
        r2 += 1
        c2 = 0
        
print(num1-num2)