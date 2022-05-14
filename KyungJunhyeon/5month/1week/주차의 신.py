for i in range(int(input())):
    count = int(input())
    listNum = list(map(int, input().split()))
    listNum.sort(reverse=True)
    total = 0
    for i in range(count):
        if i != count-1:
            total += listNum[i] - listNum[i+1]
        else:
            total += listNum[0] - listNum[count-1]
    print(total)
