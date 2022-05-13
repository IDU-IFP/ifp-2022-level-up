bugerNum = []
drinkNum = []
for _ in range(3):
    bugerNum.append(int(input()))
for _ in range(2):
    drinkNum.append(int(input()))
print(min(bugerNum)+min(drinkNum))
