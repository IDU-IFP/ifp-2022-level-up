num = []
temp = 0
for i in range(5):
    num.append(int(input()))
result = sum(num)
print(round(result / len(num)))
num.sort()
print(num[2])
