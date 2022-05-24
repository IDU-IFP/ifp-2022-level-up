# 예제를 통한 유추
"""
    입력 : 첫째 줄 N (1 <= N <= 100)
    출력 : 첫째 줄부터 차례대로 별 출력
"""
typed = int(input())
star = ["* " * typed for _ in range(typed)]

for a, b in enumerate(star):
    if a % 2 == 0:
        print(b[:2 * typed - 1])
    
    else:
        print(f" {b[:2 * typed - 1]}")