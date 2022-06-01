n, k = list(map(int, input().split()))
coin = []
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
res = 0

for i in coin:
    res += k // i
    k = k % i

print(res)
