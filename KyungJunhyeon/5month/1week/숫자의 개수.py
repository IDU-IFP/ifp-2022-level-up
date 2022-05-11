A = int(input())
B = int(input())
C = int(input())
mixNum = A * B * C
mixNumList = list(map(int, str(mixNum)))
for i in range(10):
    print(mixNumList.count(i))
