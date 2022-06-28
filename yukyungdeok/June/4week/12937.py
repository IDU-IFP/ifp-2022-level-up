# 12937번 짝수와 홀수(프로그래머스)
def solution(num):
    answer = ''
    
    if (num % 2) == 0:
        answer = "Even"
    else:
        answer = "Odd"
    
    return answer