for i in range(int(input())):
    byNumList = []
    pos = []
    data = int(input())
    while data != 1:
        byNumList.append(data % 2)
        data = int(data / 2)
    byNumList.append(1)
    pos = [i for i in range(len(byNumList)) if byNumList[i] == 1]
    print(*pos, end="\n")
