# 카드 게임

total = 0 # 총점을 담을 변수 선언

# 5회의 게임에서 얻은 점수를 순차적으로 덧셈
for _ in range(5):
    total += int(input())

# 출력
print(total)