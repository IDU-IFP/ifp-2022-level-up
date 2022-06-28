N = []

for i in range(10):
    a = int(input())
    b = a % 42
    N.append(b)

AND = set(N)
print(len(AND))