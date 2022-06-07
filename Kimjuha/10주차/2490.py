import sys
input = sys.stdin.readline

point = {0: "E", 1: "A", 2: "B", 3: "C", 4: "D"}

for _ in range(3):
    print(point[4-sum(list(map(int, input().split())))])
