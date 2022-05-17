# 하나의 플러그, N개의 멀티탭. 최대 몇 대의 컴퓨터를 연결할 수 있을까?
"""
    입력 : 첫째 줄에 멀티탭의 개수 N (1 <= N <= 500000)
            둘째 줄 N개의 줄에 각 몇개의 플러그를 꽂을 수 있는지 자연수가 나타남. (c < 1000)
    출력 : 첫쨰 줄에 최대로 전원에 연결될 수 있는 컴퓨터 수
"""
import sys
PLUGED = 1

def plugedIn():
    temp = 0

    for a in range(int(sys.stdin.readline())):
        typed = int(sys.stdin.readline())
        temp += typed - PLUGED

    print(temp + PLUGED)

plugedIn()