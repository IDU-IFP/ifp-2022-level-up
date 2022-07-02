NUM = []

for i in range(10):
    NUM.append(int(input()))

AVERAGE = sum(NUM)/10
print('%.f' % AVERAGE)

MODE = max(set(NUM), key = NUM.count)
print(MODE)
