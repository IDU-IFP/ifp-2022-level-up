#https://www.acmicpc.net/problem/10178

for _ in range(int(input())):
    c,v = map(int,input().split())
    print("You get",c//v,"piece(s) and your dad gets",c%v,"piece(s).")