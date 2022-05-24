def listOfNumber():
    tempList = []
    for i in range(10):
        tempList.append(int(input()))
    return tempList


wUni = listOfNumber()
kUni = listOfNumber()

wUni.sort(reverse=True)
kUni.sort(reverse=True)

print(sum(wUni[0:3]), sum(kUni[0:3]))
