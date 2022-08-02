import math


def solution(n):
    answer = math.sqrt(n)
    answer = str(answer)
    answer = list(map(int, answer.split(".")))

    if answer[1] == 0:
        finalAnswer = (int(answer[0])+1) ** 2
    else:
        finalAnswer = -1
    return finalAnswer
