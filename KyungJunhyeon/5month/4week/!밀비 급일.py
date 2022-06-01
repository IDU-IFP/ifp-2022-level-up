allString = []

while(1):
    string = input()
    if string == "END":
        break
    else:
        temp = list(string)
        temp.reverse()
        joinedTemp = "".join(temp)
        allString.append(joinedTemp)

for i in allString:
    print(i)
