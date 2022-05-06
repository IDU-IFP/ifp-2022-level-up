count = int(input())
oddEven = 0
for i in range(1, count+1, 1):
    if count == 1:
        print("*", end="")
    else:
        for j in range(1, count+1, 1):
            if oddEven == 0 and j != count:
                print("*", end="")
                print(" ", end="")
            elif oddEven == 1 and j != count:
                print(" ", end="")
                print("*", end="")
            elif oddEven == 0 and j == count:
                print("*")
            elif oddEven == 1 and j == count:
                print(" *")

    if oddEven == 0:
        oddEven = 1
    else:
        oddEven = 0    