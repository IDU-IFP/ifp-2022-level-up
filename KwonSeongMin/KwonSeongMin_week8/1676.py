#https://www.acmicpc.net/problem/1676

n = int(input())
s = 1
c = 0
for i in range(1,n+1):
    s *= i

for i in reversed(str(s)):  # 수를 뒤집어서 보기
    if i == '0':
        c += 1
    else:
        break
    
print(c)