# 첫째 줄에는 별 1개, 둘째 줄에는 별 3개... N번째 줄에는 2*N - 1개의 별을 찍는다. 별은 가운데 기준 정렬
"""
    입력 : 첫째 줄에는 N (1 <= N <= 100)
    출력 : 첫째 줄부터 N번째 줄까지 차례대로 별을 출력
"""
typed = int(input())
half = int(typed + 0.5)
for a in range(1, typed + 1):
    print(" " * (half - a) + "*" * (a * 2 - 1))