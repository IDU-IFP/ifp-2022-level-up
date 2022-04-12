def d(num):
    sum = num
    while num > 0:
        sum += num % 10
        num //= 10
    if sum < 10000:
        return sum

for i in range(1,10001):
    print(d(i))

    