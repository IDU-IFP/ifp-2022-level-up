resultList = []
for i in range(int(input())):
    tempList = []
    alphaList = list(input())
    tempStr = []
    for strWord in alphaList:
        tempStr.append(ord(strWord))

    if tempStr[0] > 96:
        tempStr[0] -= 32
    else:
        pass

    tempOrd = []
    for ordWord in tempStr:
        tempOrd.append(chr(ordWord))

    string = "".join(tempOrd)
    tempList.append(string)
    string = " ".join(tempList)
    resultList.append(string)
for i in resultList:
    string = "".join(i)
    print(string)


# resultList = []
# for i in range(int(input())):
#     tempList = []
#     alphaList = list(map(str, input().split()))
#     for alphaWord in alphaList:
#         tempStr = []
#         for strWord in alphaWord:
#             tempStr.append(ord(strWord))

#         if tempStr[0] > 96:
#             tempStr[0] -= 32
#         else:
#             pass

#         tempOrd = []
#         for ordWord in tempStr:
#             tempOrd.append(chr(ordWord))

#         string = "".join(tempOrd)
#         tempList.append(string)
#     string = " ".join(tempList)
#     resultList.append(string)
# for i in resultList:
#     string = "".join(i)
#     print(string)


# def strToOrd(listName):
#     tempList = []
#     for i in listName:
#         tempList.append(ord(i))
#     return tempList


# def ordToStr(listName):
#     tempList = []
#     for i in listName:
#         tempList.append(chr(i))
#     return tempList


# def ordToRevers(listName):
#     finalList = []
#     for i in listName:
#         if i < 96 and i != 32:
#             finalList.append(i+32)
#         elif i == 32:
#             finalList.append(i)
#         else:
#             finalList.append(i-32)
#     return finalList


# def joinList(listName):
#     string = "".join(listName)
#     return string


# chrList = []

# for i in range(int(input())):
#     strInput = input()
#     strList = list(strInput)

#     tempList = strToOrd(strList)
#     ordList = ordToRevers(tempList)
#     chrList.append(ordToStr(ordList))


# for i in range(len(chrList)):

#     chrSet = joinList(chrList[i])
#     print(chrSet)

# ?????? ?????????????????? ???????????? ???????????? ????????? ??????????????? ?????????????????? ???????????? ??????.


# resultList = []
# for i in range(int(input())):
#     tempList = []
#     alphaList = list(map(str, input().split()))
#     for alphaWord in alphaList:
#         tempStr = []
#         for strWord in alphaWord:
#             tempStr.append(ord(strWord))

#         if tempStr[0] > 96:
#             tempStr[0] -= 32
#         else:
#             pass

#         tempOrd = []
#         for ordWord in tempStr:
#             tempOrd.append(chr(ordWord))

#         string = "".join(tempOrd)
#         tempList.append(string)
#     string = " ".join(tempList)
#     resultList.append(string)
# for i in resultList:
#     string = "".join(i)
#     print(string)

# ????????? ?????????????????? ?????? ???????????? ????????? ???????????? ???????????? ??? ???????????? ???????????? ??????
