# 1978번 소수 찾기
n = int(input())
a = list(map(int, input().split(' ')))
num_count = 0 

for i in a:
    count = 0 
    if(i == 1):
        continue
    for j in range(2, i+1):
        if(i % j == 0):
            count += 1
    if(count == 1):
        num_count += 1
print(num_count)