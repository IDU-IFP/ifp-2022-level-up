# 평균 학점 구하기.
"""
    입력 : 첫번쨰 줄에는 학기의 수 T
        두번째 줄에는 T개의 학기에 대한 정보
        각 학기의 정보는 다음과 같이 구성되어 있다. 
            첫번째 줄에 들었던 과목의 수 N
            다음 N개의 줄에 걸쳐 N개의 과목들의 학점 C와 성적 G가 주어진다. (1 <= N <= 10, 1 <= C <= 6)
            G는 {0, 0.7, 1, 1.3, 1.7, ... , 4, 4.3} 중 하나. 소수 부분은 최대 한자리까지만
    출력 : 각 학기에 대해 근우의 총 학점과 평점 GPA 을 출력. 정답과 절대 오차는 10^-1까지 허용
"""

CREDIT = 0
GRADE = 1
total_semester = int(input())


def totalSemesterInfo(total_semester):
    subject_info = []
    credit = []
    grade = []

    for _ in range(total_semester):
        
        semester_info = int(input())

        for _ in range(semester_info):
            
            splited = splitInfo(input())
            credit.append(int(splited[0]))
            grade.append(float(splited[1]))

        subject_info.append([credit, grade])

        credit = []
        grade = []

    return subject_info

def splitInfo(info):
    return info.split(" ")

def resultPrinter(total, info):
    for a in range(total):
        print(f"{sumTotal(info[a][CREDIT])} {round(avgGrade(info, a), 1)}")

def avgGrade(semester, which_semester):
    sum = 0

    credit = semester[which_semester][CREDIT]
    grade = semester[which_semester][GRADE]

    for x, y in zip(credit, grade):
        sum += x * y
    
    return sum / sumTotal(semester[which_semester][CREDIT])

def sumTotal(numbers):
    sum = 0

    for a in numbers:
        sum += a

    return sum


semester_info = totalSemesterInfo(total_semester)
resultPrinter(total_semester, semester_info)