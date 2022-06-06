#https://www.acmicpc.net/problem/5218

for _ in range(int(input())):
    a,b = input().split()
    print("Distances: ",end='')
    for i in range(len(a)):
        res = ord(b[i])-ord(a[i])   # b - a
        if res < 0:
            res = 26 + res  # 음수가 됐을 때
        print(res,end=" ")
    print() # 줄 바꿈