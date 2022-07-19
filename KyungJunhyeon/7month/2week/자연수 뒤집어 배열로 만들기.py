def solution(n):
    n = str(n)
    answerStr = list(n)
    answerInt = list(map(int, answerStr))
    answerInt.reverse

    return answerInt
