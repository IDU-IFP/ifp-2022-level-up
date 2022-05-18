#https://www.acmicpc.net/problem/3040

height = [0,0,0,0,0,0,0,0,0]
flag = 0

for i in range(9):
    h = int(input())
    height[i] = h

s = sum(height)

for i in range(9):
    for j in range(9):
        if s - height[i] - height[j] == 100:
            height[i] = height[j] = 0
            flag = 1
            break
    if flag:
        break
    
for res in height:
    if res: 
        print(res)