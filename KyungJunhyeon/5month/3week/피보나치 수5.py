seedPibo = [0, 1]

for i in range(2, 21):
    seedPibo.append(seedPibo[i-2]+seedPibo[i-1])

print(seedPibo[int(input())])
