# 3058번 짝수를 찾아라
n = int(input())

for _ in range(n):
    even_num = []
    numbers = list(map(int, input().split()))
    for i in numbers:
        if i % 2 == 0:
            even_num.append(i)
    print(sum(even_num), min(even_num))