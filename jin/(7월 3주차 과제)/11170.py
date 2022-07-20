for _ in range(int(input())):
    N, M = map(int, input().split())
    SUM = 0
    for i in range (N, M+1):
        NUM = list(str(i))
        if '0' in NUM:
            SUM += NUM.count('0')
    print(SUM)