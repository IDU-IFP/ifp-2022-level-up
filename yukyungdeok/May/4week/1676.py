# 1676번 팩토리얼 0의 개수
n=int(input())

z=0
while n>0:
  z+=n//5
  n//=5

print(z)