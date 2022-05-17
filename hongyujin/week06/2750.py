N = int(input())
num = []

for _ in range(N):
    num.append(int(input()))
    num.sort()    # 오름차순으로 정렬해주는 함수

for i in num:
    print(i)
