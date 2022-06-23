case=int(input())
for _ in range (case):
    store=int(input())
    storeLocal=list(map(int,input().split()))
    print((max(storeLocal)-min(storeLocal))*2)