cnt=[]
for i in range(10):
    number=int(input())%42
    if cnt.count(number)==0:
        cnt.append(number)

print(len(cnt))