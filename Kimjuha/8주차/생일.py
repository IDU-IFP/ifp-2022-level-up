import sys
input = sys.stdin.readline

n = int(input())
birth = []

for i in range(n):
    name, date, mon, year = input().split()
    date, mon, year = map(int, (date, mon, year))
    birth.append((year, mon, date, name))

birth.sort()

print(birth[-1][3])
print(birth[0][3])
