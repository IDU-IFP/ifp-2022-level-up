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

# 문제 잘못이해해서 대소문자 바꾸는걸 여러개 해주는걸로 컨버트했는데 아까워서 놔둠.


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

# 이것도 잘못이해했네 ㅋㅋ 띄어쓰기 구분된 문자열의 앞글자를 다 대문자로 바꿔주는 코드
