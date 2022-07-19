def Rev(number):
    result=""
    while number!=0:
        result+=str(number%10)
        number=number//10
    return int(result)


x,y=map(int,input().split())
print(Rev(Rev(x)+Rev(y)))