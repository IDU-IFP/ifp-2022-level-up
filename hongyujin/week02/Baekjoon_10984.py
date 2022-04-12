t = int(input())  # 학기의 수 입력

for _ in range(t):  # t 반복문
    n = int(input())  # 과목의 수
    credit = 0
    grade = 0

for _ in range(n):
    c, g = map(float, input().split())
    credit += int(c)
    grade += float(c) * float(g)  # 성적은 float로 바꿔서 계산
    # round는 반올림응 해주는 함수이고 소수점 1번째 자리까지 받음
    GPA = round(grade / credit, 1)
    print(credit, GPA)
