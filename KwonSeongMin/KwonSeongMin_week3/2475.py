#https://www.acmicpc.net/problem/2475
sum = 0
n = list(map(int,input().split()))
for i in range(5):
    sum += n[i] * n[i]
print(sum%10)

#or

f = 0
a, b, c, d, e = map(int, input().split())
f += a*a + b*b + c*c + d*d + e*e
print(f % 10)