count = 0
totalCount = 0
num = int(input())
check = list(map(int, input().split()))
for i in range(num):
    if check[i] == 0:
        count = 0
    else:
        count += 1
        totalCount += count
print(totalCount)
