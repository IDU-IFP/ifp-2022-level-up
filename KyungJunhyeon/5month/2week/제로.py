import sys

numList = []
forNum = int(sys.stdin.readline())
for i in range(forNum):
    num = int(sys.stdin.readline())
    if num == 0:
        numList.pop()
    else:
        numList.append(num)
print(sum(numList))
