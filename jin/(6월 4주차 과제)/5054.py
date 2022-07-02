T = int(input())

for i in range(T):
    a = int(input())
    b = list(map(int, input().split()))
    c = sum(b)//a
    d = []

    for j in range(len(b)):
        d.append((b[j] - c)*2)
    
    print(abs(min(d))+abs(max(d)))
    