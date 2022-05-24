#https://www.acmicpc.net/problem/1357

a,b = input().split()
rev = str(int(a[::-1])+int(b[::-1]))    #문자열 뒤집어서 int형으로 계산후, str로 변환
print(int(rev[::-1]))   #문자열 뒤집어서 int로 출력(0으로 시작하는 것을 방지)
