# 12928번 약수의 합 (프로그래머스)
def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        if n % i == 0:
            answer += i

    return answer