CCount = 0
GPA = 0.0
T = int(input())
for i in range(T):
    N = int(input())
    for i in range(N):
        C, G = map(float, input().split())
        C = int(C)
        CCount += C
        GPA += C*G
        total = GPA / CCount
    print(CCount, round(total,1))

