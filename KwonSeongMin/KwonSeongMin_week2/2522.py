#https://www.acmicpc.net/problem/2522

a = int(input())
for i in range(-a+1,a):
    b = abs(i)
    print(" "*b+"*"*(a-b))