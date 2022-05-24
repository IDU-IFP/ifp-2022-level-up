#https://www.acmicpc.net/problem/2576
min=100
sum=0
for _ in range(7):
    n=int(input())
    if(n%2!=0):
        if min>n:
            min=n
        sum+=n
if not sum:
    print(-1)
    quit()
print(sum)
print(min)