import sys
sys.stdin.readline()

checked = "".join(sys.stdin.readline().split())
zero_split = checked.split("0")

result = 0

for a in zero_split:
    result += (len(a) * (len(a) + 1)) / 2

print(int(result))