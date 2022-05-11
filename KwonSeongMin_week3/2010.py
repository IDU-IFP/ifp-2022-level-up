#https://www.acmicpc.net/problem/2010
import sys
sum = 0
for _ in range(int(sys.stdin.readline())):
    sum += int(sys.stdin.readline()) - 1
print(sum+1)