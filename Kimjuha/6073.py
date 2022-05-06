number = map(int, input().split())

for element in number:
    if element != 0:
        print(element)
        continue
    break
