#https://www.acmicpc.net/problem/5565

money = int(input())
for _ in range(9):
    money -= int(input())
    
print(money)