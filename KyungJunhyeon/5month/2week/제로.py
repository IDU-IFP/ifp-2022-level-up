numList = []
for i in range(int(input())):
    num = int(input())
    if num == 0:
        numList.pop()
    else:
        numList.append(num)
print(sum(numList))
