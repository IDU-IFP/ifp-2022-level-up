import sys
input = sys.stdin.readline
case = int(input())
for i in range(case):
    numbers = []
    int(input())
    numbers = map(int, input().split())

    print(sum(numbers))
