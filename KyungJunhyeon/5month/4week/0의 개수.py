for _ in range(int(input())):
    counter = 0
    N, M = map(int, input().split())
    for j in range(N, M+1):
        tempString = str(j)
        tempList = list(tempString)
        counter += tempString.count("0")

    print(counter)
