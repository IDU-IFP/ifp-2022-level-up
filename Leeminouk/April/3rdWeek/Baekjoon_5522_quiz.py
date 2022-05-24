# JOI 는 카드 게임 중 5회 진행 중 총점을 승부함.
"""
    입력 : i 번째 줄 (1 <= i <= 5) 에 정수 A(i) i 번째 게임의 점수
    출력 : 총점을 출력 (0 <= A <= 100)
"""
import sys

def totalScore():
    total = 0

    for _ in range(5):
        typed = int(sys.stdin.readline())
        total += typed

    print(total)

totalScore()
