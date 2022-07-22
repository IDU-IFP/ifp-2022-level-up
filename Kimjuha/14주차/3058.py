case=int(input())
for _ in range (case):
    allNum=list(map(int,input().split()))
    even=[]
    for i in allNum:
        if i%2==0:
            even.append(i)
        
    even.sort()
    print(sum(even),min(even))