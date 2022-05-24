# 0보다 크거나 같은 정수 N. N! 출력
"""
    입력 : 첫째 줄에 정수 N (0 <= N <= 12)
    출력 : 첫째줄에 N! 출력
"""
typed = int(input())

def factorialN(number):
    return 1 if number == 0 else factorialN(number - 1) * number

print(factorialN(typed))