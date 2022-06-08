a=int(input())
for i in range(a):
    price=int(input())
    total=price
    count=int(input())
    for _ in range(count):
        case,option=map(int,input().split())
        total+=case*option
    
    print(total)