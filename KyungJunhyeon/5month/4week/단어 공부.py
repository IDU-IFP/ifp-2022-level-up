from copy import deepcopy


def strToOrd(listName):
    tempList = []
    for i in listName:
        tempList.append(ord(i))
    return tempList


def ordToStr(listName):
    tempList = []
    for i in listName:
        tempList.append(chr(i))
    return tempList


def ordToRevers(listName):
    finalList = []
    for i in listName:
        if i > 96:
            finalList.append(i-32)
        else:
            finalList.append(i)
    return finalList


def joinList(listName):
    string = "".join(listName)
    return string


strInput = input()
strList = list(strInput)

tempList = strToOrd(strList)
ordList = ordToRevers(tempList)
chrList = ordToStr(ordList)

chrNum = deepcopy(chrList)
chrNum = list(set(chrNum))

temp = 0
tag = ""
for Num in chrNum:
    if temp < chrList.count(Num):
        temp = chrList.count(Num)
        tag = Num
    elif temp == chrList.count(Num):
        tag = "?"

print(tag)
