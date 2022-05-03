for i in range(int(input())):
    totalPrice = int(input())
    for j in range(int(input())):
        optionCount, optionPrice = map(int, input().split())
        totalPrice += (optionCount * optionPrice)
    print(totalPrice)
