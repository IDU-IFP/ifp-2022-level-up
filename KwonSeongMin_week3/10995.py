#https://www.acmicpc.net/problem/10995
n = int(input())
for i in range(n):
    if i%2 != 0:
        print(" ",end='')
    print("* "* n)