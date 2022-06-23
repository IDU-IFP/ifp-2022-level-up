import sys
count = int(sys.stdin.readline())
total = 0
for i in range(count):
    total += int(sys.stdin.readline())

print(total-count+1)
