#https://www.acmicpc.net/problem/2460

m, n = 0, 0
for _ in range(10):
    o, i = map(int, input().split())
    n = n - o + i   # plus input, minus output
    if n > m:   # 가장 많을 때를 구함
        m = n
print(m)
