#https://www.acmicpc.net/problem/2446

a = int(input())
for i in range(1-a, a):
    b = abs(i)
    print(" "*(a-b-1)+"*"*((b*2)+1))
