T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))
    even = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)

    print(sum(even), min(even))
