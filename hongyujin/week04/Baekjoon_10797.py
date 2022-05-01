import sys
input = sys.stdin.readline

day = int(input())
car = list(map(int, input().split()))
count = 0  # 위반하는 차량 수

for i in range(len(car)):
    if car[i] == day:  # 해당 차 번호가 날짜와 일치하면
        count += 1  # count를 1 증가

print(count)
