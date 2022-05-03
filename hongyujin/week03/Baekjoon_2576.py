import sys
imput = sys.stdin.readline  # input()는 시간초과 발생
s = []

for i in range(7):
    n = int(input())
    if n % 2 != 0:
        s.append(n)
if s:
    print(sum(s))
    print(min(s))
else:
    print(-1)
