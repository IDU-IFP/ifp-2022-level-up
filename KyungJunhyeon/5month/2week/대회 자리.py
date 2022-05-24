for _ in range(int(input())):
    numList = []
    P, M = map(int, input().split())
    for _ in range(P):
        numList.append(int(input()))
    numList = list(set(numList))
    print(P - len(numList))
#M이 없네요