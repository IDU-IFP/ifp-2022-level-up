import sys
input = sys.stdin.readline

A = int(input())
B = list(map(int, input().split()))

score = 1
totalScore = 0

for i in range (A):
    if B[i] == 1:
        totalScore += score
        score += 1

    elif B[i] == 0:
        score = 1

print(totalScore)