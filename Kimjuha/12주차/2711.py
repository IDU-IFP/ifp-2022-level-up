case=int(input())
for i in range (case):
    num,spell=input().split()
    num=int(num)-1
    print(spell[:num]+spell[num+1:])