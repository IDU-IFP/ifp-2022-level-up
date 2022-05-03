# 주사위 게임
"""
    입력 : 테스트 케이스 T
            각 체스트 케이스는 2번 던져 나온 두 수가 입력
    출력 : Case x: 두 주사위 수의 합
"""
import sys
typed = int(sys.stdin.readline())
temp = []

for _ in range(typed):
    dice_one, dice_two = [int(a) for a in sys.stdin.readline().split()]
    temp.append(dice_one + dice_two)

for a in range(typed):
    print(f"Case {a + 1}: {temp[a]}")