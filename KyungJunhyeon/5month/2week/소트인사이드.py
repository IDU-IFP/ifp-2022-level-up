num = input()
listNum = list(num)
listNum.sort(reverse=True)
for i in listNum:
    print(i, end="")
