string = input()
stringList = list(string)
tempList = []
for i in range(int(len(stringList) / 10)+1):
    if i != int(len(stringList) / 10):
        string = "".join(stringList[i*10:(i+1)*10])
        tempList.append(string)
    else:
        string = "".join(stringList[i*10:])
        tempList.append(string)
for tempString in tempList:
    print(tempString)
