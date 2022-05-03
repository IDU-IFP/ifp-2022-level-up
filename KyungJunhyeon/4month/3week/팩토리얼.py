pakNum = int(input())
count = 1
for i in range(1, pakNum+1):
    if pakNum == 0:
        print("1")
    else:
        count = count*i
print(count)
