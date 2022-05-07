# 플러그

import sys # 시간 초과 방지를 위한 sys 불러오기

n = int(sys.stdin.readline()) # 멀티탭의 개수 입력
multitap = [] # 각 멀티탭의 플러그 개수를 담을 변수 선언
res = 0 # 전원에 연결될 수 있는 컴퓨터의 수 출력

# 각 멀티탭의 플러그 개수 입력
for i in range(n):
    plug = int(sys.stdin.readline())
    multitap.append(plug)

# 전원에 연결될 수 있는 컴퓨터의 수 구하기
for e in range(n):
    if(e == n - 1):
        res += multitap[e]
    else:
        res += multitap[e] - 1

# 출력
print(res)