# 11170번 0의 개수
for _ in range(int(input())):
    z = 0
    n, m = input().split()
    for i in range(int(n), int(m)+1):
        z += str(i).count('0')
    print(z)