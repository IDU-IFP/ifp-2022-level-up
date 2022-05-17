# 문제
# 한상덕은 이번에 중덕 고등학교에 새로 부임한 교장 선생님이다. 교장 선생님으로서 첫 번째 일은 각 반의 수학 시험 성적의 통계를 내는 일이다.

# 중덕 고등학교 각 반의 학생들의 수학 시험 성적이 주어졌을 때, 최대 점수, 최소 점수, 점수 차이를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 중덕 고등학교에 있는 반의 수 K (1 ≤ K ≤ 100)가 주어진다. 다음 K개 줄에는 각 반의 학생수 N (2 ≤ N ≤ 50)과 각 학생의 수학 성적이 주어진다. 시험 성적은 0보다 크거나 같고, 100보다 작거나 같은 정수이고, 공백으로 나누어져 있다. 

# 출력
# 각 반에 대한 출력은 다음과 같이 두 줄로 이루어져 있다.

# 첫째 줄에는 "Class X"를 출력한다. X는 반의 번호이며 입력으로 주어진 순서대로 1부터 증가한다.
# 둘째 줄에는 가장 높은 점수, 낮은 점수, 성적을 내림차순으로 정렬했을 때 가장 큰 인접한 점수 차이를 예제 출력과 같은 형식으로 출력한다.

import sys

typed = sys.stdin.readline

school_class = int(typed())

for i in range(school_class):
    student_info = input().split()
    student, scores = int(student_info[0]), list(map(int, student_info[1:]))

    scores.sort(reverse=True)
    largest_gap = 0

    for j in range(len(scores) - 1):
        if (scores[j] - scores[j + 1]) > largest_gap:
            largest_gap = scores[j] - scores[j + 1]

    print("Class", i + 1)
    print(f"Max {scores[0]}, Min {scores[len(scores) - 1]}, Largest gap {largest_gap}")