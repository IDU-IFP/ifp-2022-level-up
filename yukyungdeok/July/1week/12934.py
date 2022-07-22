# 12934번 정수 제곱근 판별(프로그래머스)
def solution(n):
    sqrt = n ** (1/2)
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1