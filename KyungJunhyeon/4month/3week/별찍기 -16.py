height = int(input())
for i in range(0, height):
    if height == 1:
        print("*", end="")
    else:
        for _ in range(height, i+1, -1):
            print(" ", end="")
        for j in range(i+1):
            if j != height:
                print("*", end="")
                print(" ", end="")
            elif j == height:
                print("*")
    print("")
