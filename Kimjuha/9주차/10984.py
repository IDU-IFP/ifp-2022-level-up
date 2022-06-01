a=int(input())
for _ in range(a):
    b=int(input())
    total1=total2=0
    for i in range(b):
        sun,aver=map(float,input().split())
        total1+=sun
        total2+=aver*sun
    
    print(int(total1),'%.1f'%(total2/total1))