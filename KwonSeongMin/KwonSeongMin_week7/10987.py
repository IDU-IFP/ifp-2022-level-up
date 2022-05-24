#https://www.acmicpc.net/problem/10987

arr = ['a','e','i','o','u']
count = 0
word = input()

for i in word:
    if i in arr:
        count += 1
        
print(count)
        
        