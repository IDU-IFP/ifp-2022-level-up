a, d, n = map(int, input().split())

i = a
count = 0
arith = []
while count < n:
    arith.append(i)
    i += d
    count += 1
print(arith[-1])
