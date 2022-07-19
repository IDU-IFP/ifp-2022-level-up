case=int(input())
money=[]
for i in range (case):
    price=int(input())
    if price!=0:
        money.append(price)
    else:
        money.pop()
        
print(sum(money))