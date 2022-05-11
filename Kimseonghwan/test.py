# 2592번 대표값
n = [int(input()) for _ in range(10)]

print(round(sum(n)/10))
print(max(n, key=n.count))
