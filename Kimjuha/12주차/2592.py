numbers=[]

for i in range (10):
    numbers.append(int(input()))
    
    
print(int(sum(numbers)/10))
print(max(numbers,key=numbers.count))