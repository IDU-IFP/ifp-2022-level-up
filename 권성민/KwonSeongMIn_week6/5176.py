#https://www.acmicpc.net/problem/5176

for _ in range(int(input())):
    seat = []
    count = 0
    p,m = map(int,input().split())
    for i in range(p):
        s = int(input())
        if s in seat:   #좌석이 겹치면 
            count += 1  #count
        else:   #안 겹치면
            seat.append(s)  #앉힘  
    print(count)