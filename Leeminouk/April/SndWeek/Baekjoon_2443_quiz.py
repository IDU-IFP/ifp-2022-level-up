# 첫째 줄 별 2 * N - 1, 둘째 줄 별 2 * N - 3 ...
"""
    입력 : 첫째 줄 N (1 <= N <= 100)
    출력 : 첫째 줄부터 N 번째 줄까지 차례대로 별을 출력
"""
typed = int(input())
for a in range(typed, 0, -1):
    print(" " * (typed - a) + "*" * (a * 2 - 1))