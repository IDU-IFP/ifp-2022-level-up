inputNumber = int(input())
count = 2
while(1):
    if inputNumber != 1:
        if inputNumber % count == 0:
            print(count)
            inputNumber = int(inputNumber / count)
        else:
            count += 1
    else:
        break
