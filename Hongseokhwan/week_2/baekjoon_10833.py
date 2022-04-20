# 사과

n = int(input()) # 학교의 수 입력
rest = 0 # 남는 사과 개수를 담을 변수 선언

# 남는 사과 개수의 최소값을 저장
for _ in range(0,n):
    student, apple = map(int, input().split(" "))
    rest += apple % student

# 학교별 남은 사과 개수의 합 출력
print(rest)