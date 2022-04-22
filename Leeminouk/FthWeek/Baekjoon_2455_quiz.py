import sys

result = 0
temp = 0

for _ in range(4):
    outside, inside = sys.stdin.readline().split()

    temp = int(inside) - int(outside) + temp

    if temp > result:
        result = temp

print(result)