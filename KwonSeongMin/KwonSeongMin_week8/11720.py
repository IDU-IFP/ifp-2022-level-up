#https://www.acmicpc.net/problem/11720

sum = 0
c = int(input())
l = input() # 먼저 문자열 형태로 입력 받기
for n in l:
    sum += int(n)   #배열 한칸부위별로 더해주기
    
print(sum)