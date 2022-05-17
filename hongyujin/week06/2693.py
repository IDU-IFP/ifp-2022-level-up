T = int(input())

for i in range(T):
    n = list(map(int, input().split()))
    n.sort()
    print(n[-3])  # 오름차순 정렬이여서 뒤에서 3번째
