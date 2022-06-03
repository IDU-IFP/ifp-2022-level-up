input()
temp = 0
stringNumber = str(input())
tempList = list(stringNumber)
for i in tempList:
    temp += int(i)
print(temp)
