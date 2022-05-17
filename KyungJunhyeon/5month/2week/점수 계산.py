costList = []
sortList = []
for i in range(8):
    costList.append(int(input()))
sortedCostList = costList.copy()
sortedCostList.sort()

for sortNum in sortedCostList[len(sortedCostList)-5:]:
    sortList.append(costList.index(sortNum)+1)

sortList.sort()
print(sum(sortedCostList[len(sortedCostList)-5:]))
print(*sortList)
