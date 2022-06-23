end = int(input())

total = 0
for i in range(1, end + 1):
    total += i
    if total >= end:
        print(i)
        break
