matchNum = list(map(int, input().split()))
totalCount = 0
for i in range(len(matchNum)):
    totalCount += matchNum[i] ** 2
print(totalCount % 10)
