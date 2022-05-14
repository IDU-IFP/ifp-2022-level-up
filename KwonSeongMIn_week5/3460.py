#https://www.acmicpc.net/problem/3460

for _ in range(int(input())):
    res = []
    t = int(input())
    while t:
        res.append(t%2)
        t//=2
    for i in range(len(res)):
        if res[i]:
            print(i,end=' ')
    print()