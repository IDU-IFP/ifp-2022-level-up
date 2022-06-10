a=int(input())
for i in range(1,a):
    print("*"*i+" "*((a-i)*2)+"*"*i)
    
for i in range(a,0,-1):
    print("*"*i+" "*((a-i)*2)+"*"*i)