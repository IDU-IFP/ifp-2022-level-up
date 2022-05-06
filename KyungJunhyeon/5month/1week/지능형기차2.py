totalCount = []
for i in range(0, 10):
    outPeople, inPeople = map(int, input().split())
    if i == 0 or i == 9:
        totalCount.insert(i, inPeople - outPeople)
    else:
        totalCount.insert(i, totalCount[i-1] - outPeople + inPeople)
print(max(totalCount))
# 문제 2라고해서 뭔가 다를줄알았는데 같은문제네
