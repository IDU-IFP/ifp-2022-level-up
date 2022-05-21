for _ in range(int(input())):
    listNum = list(map(int, input().split()))
    listNum.remove(min(listNum))
    listNum.remove(max(listNum))
    if max(listNum) - min(listNum) >= 4:
        print("KIN")
    else:
        print(sum(listNum))

    # KIN이라고 표현하는 센스가 돋보인 문제
