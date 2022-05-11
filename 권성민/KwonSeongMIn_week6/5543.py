#https://www.acmicpc.net/problem/5543

burger = [0,0,0]
juice = [0,0]

for i in range(3):
    m = int(input())
    burger[i] = m
    
for j in range(2):
    m = int(input())
    juice[j] = m
    
burger.sort()
juice.sort()

print(burger[0] + juice[0] - 50)