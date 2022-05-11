num = []
temp = 0
mode = 0
for i in range(10):
    num.append(int(input()))
for i in num:
    if num.count(i) > temp:
        temp = num.count(i)
        mode = i
result = sum(num)
print(round(result / len(num)))
print(mode)
