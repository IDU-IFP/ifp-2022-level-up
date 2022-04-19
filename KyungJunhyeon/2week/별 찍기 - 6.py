starNum = int(input())
for i in range(starNum):
    for j in range(i):
        print(" ", end="")
    for z in range(starNum-(i+1)):
        print("*", end="")
    for y in range(starNum-(i)):
        print("*", end="")
    print("")
