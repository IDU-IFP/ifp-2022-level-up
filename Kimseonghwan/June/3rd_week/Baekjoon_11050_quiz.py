# 링크
# https://www.acmicpc.net/problem/11050

# 이항 계수 1

# 문제
# 자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수
# \(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 10, 0 ≤ \(K\) ≤ \(N\))

# 출력

# \(\binom{N}{K}\)를 출력한다.

# 예제 입력 1
# 5 2
# 예제 출력 1
# 10


# 이항계수의 정의
# nCk = n!/(n-k)!k!

# 함수 ------------------------------------------------------------
def solution(N, K):
    return int(factorial(N)/(factorial(N-K)*factorial(K)))


def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


# 실행 ------------------------------------------------------------
N, K = map(int, input().split())
print(solution(N, K))
