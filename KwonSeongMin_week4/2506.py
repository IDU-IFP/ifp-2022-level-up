#https://www.acmicpc.net/problem/2506

n=int(input())
t=list(map(int,input().split()))
s,i=0,1
for case in t:
    if case:
        s+=i
        i+=1
    else:
        i=1
print(s)