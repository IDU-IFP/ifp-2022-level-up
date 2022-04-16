# 7개의 자연수가 주어질 때, 이 수 중 홀수인 자연수를 모두 골라 합을 구하고 고른 홀수들 중 최솟값을 찾는 프로그램을 작성하시오.
"""
    입력 : 첫째 줄부터 일곱 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 
            주어지는 자연수는 100보다 작음
    출력 : 홀수가 존재하지 않는 경우에는 첫째 줄에 -1 출력. 
            홀수가 존재하는 경우 첫째 줄에 홀수의 합, 둘째 줄에는 홀수들 중 최솟값 출력
"""
import sys

SEVEN = 7
total = 0
minimum_value = 100

def calNminimumNumber():
    global total
    global minimum_value

    for _ in range(SEVEN):
        typed = int(sys.stdin.readline())

        if typed % 2 != 0:
            total += typed

            if minimum_value > typed:
                minimum_value = typed

        else:
            continue

def isNoOdd():
    return True if total == 0 and minimum_value == 100 else False

calNminimumNumber()

if isNoOdd():
    print(-1)

else:
    print(total)
    print(minimum_value)
