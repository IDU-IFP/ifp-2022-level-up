#https://school.programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    answer = 0
    num = str(n)
    for s in num:
        answer += int(s)

    return answer