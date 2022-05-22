N, K = map(int, input().split())
countList = []
numberOfCoin = 0

for i in range(N):
    countList.append(int(input()))

countList.sort(reverse=True)

for count in countList:
    if K >= count:
        numberOfCoin += int(K / count)
        K = int(K % count)

print(numberOfCoin)
