# 3040번 백설 공주와 일곱 난쟁이
import sys
input = sys.stdin.readline
s = [int(input()) for i in range(9)]
for i in range(8):
    for j in range(i + 1, 9):
        result = 0
        for k in range(9):
            if k == i or k == j:
                continue
            result += s[k]
        if result == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(s[k])
            exit()