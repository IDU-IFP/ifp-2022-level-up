for i in range(int(input())):
    x, y = input().split()
    alp = []
    for i in range(len(x)):
        if ord(x[i]) <= ord(y[i]):
            alp.append(ord(y[i]) - ord(x[i]))
        else:
            alp.append((ord(y[i]) + 26) - ord(x[i]))
    print("Distances:", *alp)
