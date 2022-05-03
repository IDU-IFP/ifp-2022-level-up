sum = 0
for n in list(map(int, input().split())):
    sum += n*n
print(sum % 10)
