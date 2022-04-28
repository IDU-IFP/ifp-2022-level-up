import sys

result = []
for _ in range(int(sys.stdin.readline())):
    sys.stdin.readline()
    result.append(sum(map(int, sys.stdin.readline().split())))

for _ in range(len(result)):
    print(result.pop(0))