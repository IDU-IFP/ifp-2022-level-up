#https://www.acmicpc.net/problem/2443

a = int(input())
for i in range(a,0,-1):
    print(" "*(a-i)+"*"*(i*2-1))
