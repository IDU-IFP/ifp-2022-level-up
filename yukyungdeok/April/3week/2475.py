# 2475번 검증수

n = 0; 
for i in map(int, input().split()): 
    n += i**2
print(n % 10)