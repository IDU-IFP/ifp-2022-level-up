# 첫째 줄에는 N개, N번째 줄에는 별 1개를 찍는 문제
"""
    입력 : 첫째 줄에는 N(1 <= N <= 100)
    출력 : 첫째 줄부터 N번째 줄까지 차례대로 별로 출력
"""
for a in map(lambda x : x * "*", [_ for _ in range(int(input()), 0, -1)]):
    print(a)