case=int(input())
number=[]
for i in range (case):
    number.append(int(input()))
number.sort()
for i in number:
    print(i)