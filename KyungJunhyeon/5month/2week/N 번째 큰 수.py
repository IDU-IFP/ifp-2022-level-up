for i in range(int(input())):
    listNum = list(map(int, input().split()))
    listNum.sort(reverse=True)
    print(listNum[2])
