a = list(map(int, input().split()))
b = 0
for i in a:
    b += i*i
 
print(b % 10)
