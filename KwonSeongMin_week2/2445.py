#https://www.acmicpc.net/problem/2445

a = int(input())
for i in range(1-a,a):
    b = abs(i)
    print("*"*(a-b)+" "*b*2+"*"*(a-b))