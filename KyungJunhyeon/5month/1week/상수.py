listNum = list(map(str, input().split()))
tempNum = 0
for i in listNum:
    temp = list(i)
    temp.reverse()
    outPut = ''.join(temp)
    outPut = int(outPut)
    if outPut > tempNum:
        tempNum = outPut
print(tempNum)
