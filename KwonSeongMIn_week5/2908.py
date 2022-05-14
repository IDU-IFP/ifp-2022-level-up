#https://www.acmicpc.net/problem/2908

num1,num2 = input().split()

n1 = num1[2] + num1[1] + num1[0]    #123 > 321
n2 = num2[2] + num2[1] + num2[0]    #456 > 654

if(int(n1) > int(n2)):print (n1)
else: print(n2)