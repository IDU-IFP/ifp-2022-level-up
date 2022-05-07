starNum = int(input())
for i in range(starNum, 0, -1):
    for j in range(i-1):
        print(" ", end="")
    for z in range(starNum-(i-1)):
        print("*", end="")
    for y in range(starNum-(i)):
        print("*", end="")
    print("")

for i in range(starNum):
    for j in range(i+1):
        print(" ", end="")
    for z in range(starNum-(i+2)):
        print("*", end="")
    for y in range(starNum-(i+1)):
        print("*", end="")
    print("")
