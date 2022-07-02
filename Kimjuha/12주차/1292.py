start,end=map(int,input().split())
numbers=[]
k=1
while len(numbers)<=end:
    for i in range(1,k+1):
        numbers.append(k)
    k+=1

print(sum(numbers[start-1:end]))