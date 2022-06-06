#https://www.acmicpc.net/problem/11721

l = input()
for i in range(len(l)):
    print(l[i],end="")
    if i%10 == 9 and i: #10번째 칸마다 끊음. 0일때 끊기는걸 대비
        print()