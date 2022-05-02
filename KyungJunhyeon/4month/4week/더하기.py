count = int(input())

for _ in range(count):
    totalList = [0] * int(input())
    totalList = list(map(int, input().split()))
    print(sum(totalList))
