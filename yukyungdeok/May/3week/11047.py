# 11047번 동전 0
n, k = map(int, input().split())
coin = []
num = 0
for _ in range(n):
    coin.append(int(input()))
for i in range(n - 1, -1, -1):
    if k == 0:
        break
    if coin[i] > k:
        continue
    num += k // coin[i]
    k %= coin[i]
print(num)