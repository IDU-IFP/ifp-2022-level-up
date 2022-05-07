# 할로윈 데이 사탕을 나누어주는데, 공평하게 나누고 남은 수를 출력
"""
    입력 : 테스트 케이스 수 입력. 
        각 테스트 케이스 마다 사탕의 개수 c, 형제 수 v 출력 (1 <= c) (v <= 1000)
    출력 : You get _ piece(s) and your dad gets _ piece(s). 형식
"""
import sys

def division():
    result = []

    for a in range(int(sys.stdin.readline())):
        candy, brother = [int(a) for a in sys.stdin.readline().split()]

        result.append((int(candy / brother)))
        result.append(candy % brother)

    return result

def printer(numbers):
    for a in range(0, len(numbers), 2):
        print(f"You get {numbers[a]} piece(s) and your dad gets {numbers[a + 1]} piece(s).")

printer(division())