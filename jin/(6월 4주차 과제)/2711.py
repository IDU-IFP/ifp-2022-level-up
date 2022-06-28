InPut = int(input())

for _ in range(InPut):
    a, b = input().split()
    a = int(a)
    print(b[:a-1], b[a:], sep='')