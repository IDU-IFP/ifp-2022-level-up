case=int(input())
for i in range (case):
    num=int(input())
    binary=[]
    while num!=0:
        binary.append(num%2)
        num=num//2
        
    
    for i in range (len(binary)):
        if binary[i]==1:
            print(i,end=" ")