# 이항 계수 1

# 팩토리얼 함수
def factorial(n):
    res = 1
    for i in range(n,0,-1):
        res *= i
    return res

n, k = map(int, input().split()) # n, k 값 입력

print(factorial(n) // (factorial(k)*factorial(n-k))) # 이항 계수 출력