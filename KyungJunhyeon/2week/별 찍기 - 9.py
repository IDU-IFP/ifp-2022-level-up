starNum = int(input())
for i in range(starNum, 0, -1):
    for y in range(starNum-(i)):
        print(" ", end="")
    for j in range(i-1):
        print("*", end="")  
    print("*", end="")
    for j in range(i-1):
        print("*", end="")
    if i == 1:    
        print("",end="")
    else:
        print("")
for i in range(starNum, 0, -1):
    for j in range(i-1):
        print(" ", end="")
    for z in range(starNum-(i)):
        print("*", end="")
    if i != starNum:
        print("*", end="")
    for y in range(starNum-(i)):
        print("*", end="")
    if i == 1:    
        print("",end="")
    else:
        print("")