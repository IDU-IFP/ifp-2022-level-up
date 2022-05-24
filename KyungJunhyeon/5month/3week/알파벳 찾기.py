alphaList = [-1 for _ in range(26)]
ascList = []

temp = input()
dataSet = list(temp)

for i in dataSet:
    ascList.append(ord(i))

for i in ascList:
    alphaList[i - 97] = ascList.index(i)

print(*alphaList)
