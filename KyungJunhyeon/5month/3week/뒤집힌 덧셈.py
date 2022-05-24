listNum = list(map(str, input().split()))
tempNum = 0
for i in listNum:
    temp = list(i)
    temp.reverse()
    outPut = ''.join(temp)
    outPut = int(outPut)
    tempNum += outPut

temp = list(str(tempNum))
temp.reverse()
tempNum = ''.join(temp)
tempNum = int(tempNum)

print(tempNum)
