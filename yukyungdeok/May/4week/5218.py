# 5218번 알파벳 거리
for _ in range(int(input())):
    x, y = input().split()
    li = []
    for i in range(len(x)):
        if ord(x[i]) > ord(y[i]):
            li.append(26 - (ord(x[i])-ord(y[i])))
        else:
            li.append(ord(y[i]) - ord(x[i]))
    print("Distances:", *li)