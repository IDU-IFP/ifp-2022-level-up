# 2750번 수 계산하기
n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
li = sorted(li)
for i in range(len(li)):
    print(li[i])