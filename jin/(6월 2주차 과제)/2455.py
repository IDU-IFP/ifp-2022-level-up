a = 0
b = 0

for _ in range(4):
    OutP, InP = map(int, input().split())
    b = b + InP - OutP
    a = max(a, b)

print(a)