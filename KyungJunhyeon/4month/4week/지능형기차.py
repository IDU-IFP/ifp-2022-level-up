totalCount = []
for i in range(0, 4):
    outPeople, inPeople = map(int, input().split())
    if i == 0 or i == 3:
        totalCount.insert(i, inPeople - outPeople)
    else:
        totalCount.insert(i, totalCount[i-1] - outPeople + inPeople)
print(max(totalCount))
