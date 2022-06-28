inthetrain = 0
list1 = []

for i in range(10):
    a, b = map(int,input('').split())

    inthetrain += b
    inthetrain -= a

    list1.append(inthetrain)

print(max(list1))