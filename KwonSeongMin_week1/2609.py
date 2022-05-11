#https://www.acmicpc.net/problem/2609
# import math
# a,b = map(int, input().split())

# print(math.gcd(a,b))
# print(math.lcm(a,b))
#----------------------------------
a, b = map(int, input().split())

if a==b:
    print(a)
    print(b)
    quit()
    
min_value = 1
i = 2

while i < max(a,b):
    if a % i == 0 and b % i == 0:
        a //= i
        b //= i
        min_value *= i
        i = 2
    else:i+=1

max_value = min_value * a * b

print(min_value)
print(max_value)
