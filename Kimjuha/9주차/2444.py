a=int(input())
for j in range(1,a):
    print(" "*(a-j)+"*"*(j*2-1))
for i in range(a,0,-1):
    print(" "*(a-i) +"*"*(i*2-1))