# 12954번 x만큼 간격이 있는 n개의 숫자(프로그래머스)
def solution(x, n):
    result = []
    for i in range(1, 1001):
        if len(result) < n:
            result.append(x*i)
            
    return result