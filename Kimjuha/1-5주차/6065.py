a, b, c = map(int, input().split())
print(*filter(lambda x: x % 2 == 0, [a, b, c]))
