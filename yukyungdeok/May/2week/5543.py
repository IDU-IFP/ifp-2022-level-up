# 5543번 상근날드
buger = []
for _ in range(3):
    buger.append(int(input()))
drink = []
for _ in range(2):
    drink.append(int(input()))
min_set = min(buger) + min(drink) - 50
print(min_set)