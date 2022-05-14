burger = []
drink = []

for i in range(0, 3):
    n = int(input())
    burger.append(n)

for i in range(0, 2):
    a = int(input())
    drink.append(a)

print(min(burger) + min(drink) - 50)
