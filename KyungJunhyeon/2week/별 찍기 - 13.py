starNum = int(input())
for i in range(1, starNum+1):
    for j in range(i):
        print("*", end="")
    print("")
for i in range(starNum-1, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")