oddList = []
oddEven = 0
for i in range(7):
    count = int(input())
    if count % 2 != 0:
        oddList.append(count)
        oddEven += 1
if oddEven == 0:
    print("-1")
else:
    print(sum(oddList))
    print(min(oddList))
