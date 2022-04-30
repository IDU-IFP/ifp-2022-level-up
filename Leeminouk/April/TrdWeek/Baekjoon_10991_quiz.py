# 예제를 통한 유추
"""
    입력 : 첫째 줄 N (1 <= N <= 100)
    출력 : 첫째 줄부터 차례대로 별 출력
"""
typed = int(input())

star = ["* " * a for a in range(1, typed + 1)]
for a, b in enumerate(star):
    print(" " * ((typed - a) - 1) + b[:((a + 1) * 2) - 1])