typed = int(input())


def eachSchoolDivApple(typed):
    left_apple = 0

    for _ in range(typed):
        info_of_apple_student = input()
        info = infoIntegerSplited(info_of_apple_student)
        print(info)
        a = info.pop()
        b = info.pop()
        left_apple += (a % b)
        print(a, b, a % b)

    return left_apple


def infoIntegerSplited(info):
    return [int(a) for a in info.split(" ")]


print(eachSchoolDivApple(typed))

"""
5
24 52
13 22
5 53
23 10
7 70
"""
