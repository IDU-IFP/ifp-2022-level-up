A, B = map(int, input().split())
count = 0
makeList = []
for i in range(1, 1001):
    for _ in range(i):
        makeList.append(i)
print(sum(makeList[A-1:B]))
