a = int(input())
b = int(input())
c = int(input())

abc = (a * b * c)
ABC = list(map(int, str(abc)))

for j in range(0,10):
    num = j
    print(ABC.count(num))