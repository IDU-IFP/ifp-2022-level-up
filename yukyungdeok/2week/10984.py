# 10984번 내 학점을 구해줘
t = int(input())

for i in range(t):
    n = int(input())
    a = 0
    b = 0
    
    for j in range(n):
        c,d = map(float, input().split())
        a += c
        b += c * d
        
    GPA = b / a
    print(int(a), '%.1f' % GPA)