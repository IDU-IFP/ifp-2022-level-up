#https://www.acmicpc.net/problem/10250

import sys

input = sys.stdin.readline
for _ in range(int(input())):
    h, w, n = map(int, input().split())
    H = (n-1)%h + 1 # 6, 10 기준 1~6 숫자 형성
    W = (n-1)//h + 1 # 단순히 n//h를 할 시 맨 처음 방 배정할 때 0형성되고, 또 +1만 해주자니 호수가 틀려짐
    print("%d%02d" % (H, W))