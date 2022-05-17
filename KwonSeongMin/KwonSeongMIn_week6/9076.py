#https://www.acmicpc.net/problem/9076

for _ in range(int(input())):
    n = list(map(int,input().split()))
    n.sort()
    if n[3] - n[1] >= 4:    # a b c d e 에서 d - b 값 비교
        print("KIN")
    else:
        print(sum(n[1:4]))  #  b c d 를 합한 값