# 2693번 N번째 큰 수
for _ in range(int(input())):
    n = list(map(int, input().split()))
    n.sort()
    print(n[-3])