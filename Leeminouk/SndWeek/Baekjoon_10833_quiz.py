# 사과를 학생들에게 배정한다. 학교마다 학생마다 사과 개수가 다름. 각 학교마다 배정된 사과를 학생들에게 똑같이 나누어줌. 
# 남는 사과 개수는 최소. 학교별로 사과 개수는 다를 수도 있음. 각 학교의 학생에게 사과를 나눠주고 남은 총 사과의 개수
"""
    입력 : 첫번째 줄에는 학교의 수 정수 N (1 <= N <= 100)
        다음 N개의 줄에는 각 학교의 학생 수와 배정된 사과의 개수를 나타내는 두 정수.
            단 학생 수와 사과 수는 모두 (1 <=), (<= 100)
    출력 : 남은 사과의 총 개수를 정수로 출력
"""
typed = int(input())


def eachSchoolDivApple(typed):
    left_apple = 0

    for _ in range(typed):
        info_of_apple_student = input()
        info = infoIntegerSplited(info_of_apple_student)
        left_apple += (info.pop() % info.pop())

    return left_apple

def infoIntegerSplited(info):
    return [int(a) for a in info.split(" ")]


print(eachSchoolDivApple(typed))