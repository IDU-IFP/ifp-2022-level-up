#https://www.acmicpc.net/problem/2444

a = int(input())
for i in range(-a, a):
    print(" "*(abs(i)-1)+"*"*(abs(i)*2-1))
