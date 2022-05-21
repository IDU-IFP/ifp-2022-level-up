temp = 0
recode = 0
for i in range(5):
    count = list(map(int, input().split()))
    if sum(count) > temp:
        temp = sum(count)
        recode = i+1
print(recode, temp)
