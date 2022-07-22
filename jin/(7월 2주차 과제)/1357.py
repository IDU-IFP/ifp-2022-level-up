a, b = map(int, input().split())
c = int(str(a)[::-1])
d = int(str(b)[::-1])
print(int(str(c + d)[::-1]))
