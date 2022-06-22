a, b, c = map(int, input().split())
print(*map(lambda num: 'odd' if num % 2 else 'even', [a, b, c]))
