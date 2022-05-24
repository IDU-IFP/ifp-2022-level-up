day = int(input())
fst_numbers = [int(a) for a in input().split()]
result = {day: 0}

for a in fst_numbers:
    if a == day:
        result[day] += 1

print(result[day]) 