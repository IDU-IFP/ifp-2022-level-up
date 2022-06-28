a=int(input())
b=int(input())
c=int(input())
count=[0,0,0,0,0,0,0,0,0,0]
numbers=list(str(a*b*c))


for i in numbers:
    i=int(i)
    count[i]+=1
    
for i in range (10):
    print(count[i])
