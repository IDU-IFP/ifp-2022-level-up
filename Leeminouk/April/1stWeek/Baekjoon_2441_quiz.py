# 첫째 줄 N개, N번째 줄 1개
"""
    입력 : 첫째 줄 N (1 <= N <= 100)
    출력 : 첫째 줄부터 N번째 줄까지 차례대로 별 출력
"""
typed = int(input())

for a in map(lambda x : x * "*", [a for a in range(typed, 0, -1)]):
    print(a.rjust(typed, " "))