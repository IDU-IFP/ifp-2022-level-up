appendListNumber = []
recode = 0
count = 0
for _ in range(10):
    appendListNumber.append(int(input()) % 42)
print(len(set(appendListNumber)))
