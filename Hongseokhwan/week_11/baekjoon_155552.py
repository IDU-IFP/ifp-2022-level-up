# 빠른 A+B

import sys

# 빠른 입력을 위해 sys.stdin.readline 으로 입력한 뒤 두 정수의 합 출력
for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)