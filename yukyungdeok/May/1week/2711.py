# 2711번 오타맨 고창영
for _ in range(int(input())):
    n, str = input().split()
    n = int(n)
    print(str[:n-1], str[n:], sep='')