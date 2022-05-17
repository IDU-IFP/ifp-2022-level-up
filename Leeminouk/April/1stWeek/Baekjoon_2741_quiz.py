# 자연수 n이 주어졌을때 1 ~ n까지 한 줄에 하나씩 출력하는 프로그램
"""
    입력 : n <= 100000
    출력 : 첫줄부터 n번째 줄까지 차례로 출력
"""

typed = int(input())

for a in range(typed):
    print(a + 1)