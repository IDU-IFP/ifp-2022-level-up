count = 1
facCount = 0
for i in range(int(input()), 1, -1):
    count = count*i

facList = list(str(count))
facList.reverse()

for i in facList:
    if i == "0":
        facCount += 1
    else:
        break

print(facCount)
