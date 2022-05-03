count = int(input())
size = 0
for i in range(1, count+1, 1):
    for j in range(i, i*2+1, 1):
        size += j
print(size)
