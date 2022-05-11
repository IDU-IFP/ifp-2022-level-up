#https://www.acmicpc.net/problem/2577

res = 1

for _ in range(3):
    num = int(input())
    res *= num
for num in range(10):
    print(str(res).count(str(num)))