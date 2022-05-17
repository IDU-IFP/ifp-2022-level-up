end_point = int(input())

total = 0
for i in range(1, end_point+1):
    total += i
    if total >= end_point:
        print(i)
        break
