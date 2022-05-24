# 예제를 통한 규칙 유추 후 별 출력
"""
    입력 : 첫째 줄에 N (1 <= N <= 100)
    출력 : 첫째 줄부터 2 * N - 1 번째 줄까지 차례대로 별 출력
"""
typed = int(input())
twice = typed * 2

for a in range(1, twice):

    if a > typed:
        print(" " * (a - typed) + "*" * (2 * (twice - a) - 1))

    else:
        print(" " * (typed - a) + "*" * (a * 2 - 1))
