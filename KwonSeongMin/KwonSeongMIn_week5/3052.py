#https://www.acmicpc.net/problem/3052

count = 0

res = [0 for _ in range(42)]
for _ in range(10):
    n = int(input())
    res[n%42] += 1

for i in res:
    if i:
        count += 1
        
print(count)