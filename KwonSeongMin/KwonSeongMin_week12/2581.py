#https://www.acmicpc.net/problem/2581

m = int(input())
n = int(input())
sum = 0
min = 10001
for i in range(m,n+1):
    t = 0;
    for j in range(1,i+1):
        if i%j==0:
            t+=1
    if t==2:
        sum += i
        if i < min:
            min = i
if min==10001:
    print(-1)
else:
    print(sum)
    print(min)