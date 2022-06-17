#https://www.acmicpc.net/problem/4948
import math
list = [1 for _ in range(246913)]

list[0] = list[1] = 0

for i in range(2, int(math.sqrt(246913))+1):
    for j in range(i, 246913, i):
        if j != i:
            list[j] = 0

t = int(input())

while t:
    c = 0
    for i in range(t+1, t*2+1):
        if list[i]:
            c += 1
    print(c)
    t = int(input())
