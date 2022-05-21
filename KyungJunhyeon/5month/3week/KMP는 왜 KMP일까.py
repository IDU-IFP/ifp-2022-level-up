KMSList = list(input().split('-'))
wordList = []
for i in KMSList:
    tempList = list(i)
    wordList.append(tempList[0])

string = "".join(wordList)
print(string)
