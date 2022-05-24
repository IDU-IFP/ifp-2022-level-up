from copy import deepcopy


sumList = []
minList = []

num = int(input())
for _ in range(num):
    oddList = list(map(int, input().split()))
    tempList = deepcopy(oddList)
    for i in range(len(tempList)):
        if (tempList[i] % 2) != 0:
            oddList.remove(tempList[i])

    sumList.append(sum(oddList))
    minList.append(min(oddList))

for i in range(num):
    print(sumList[i], minList[i])
