import random

listNum = []
for _ in range(9):
    listNum.append(int(input()))
listNum.sort()

while sum(listNum) != 100:
    testList = list(listNum)
    testList.pop(random.randrange(0, 9))
    testList.pop(random.randrange(0, 8))
    if sum(testList) == 100:
        break

for i in testList:
    print(i)


# 이름만바꾼...
