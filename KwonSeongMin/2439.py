#https: // www.acmicpc.net/problem/2439

count = int(input())

for i in range(count):
    print(" "*(count-i-1)+"*"*(i+1))
