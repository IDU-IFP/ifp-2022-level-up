#https://www.acmicpc.net/problem/4458

for _ in range(int(input())):
    l = list(input())
    l[0] = l[0].upper() #첫 글자만 대문자로
    print(''.join(l))