# 첫째 줄에 별 1개, 둘째 줄에 별 2개, N번째 줄에 별 N개
"""
    입력 : 첫째 줄에 N (1 <= N <= 100)
    출력 : 첫째 줄부터 N번째 줄까지 차례대로 별을 출력
"""
typed_int = int(input())

for a in range(1, typed_int + 1):
    star = "*" * a
    print(star.rjust(typed_int, " "))
