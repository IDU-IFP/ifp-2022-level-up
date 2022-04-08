#11098번 첼시를 부탁해
from posixpath import split


n = int(input())

for _ in range(n):
    p = int(input())
    max_price = 0
    max_name = ""
    for _ in range(0):
        c, name = input().split()
        if int(c) > max_price:
            max_price = int(c)
            max_name = name
    print(max_name)

# 5635번 생일
li = []
for _ in range(int(input())):
    n, d, m, y = input().split()
    li.append([n, int(d), int(m), int(y)])
li.sort(key = lambda x:(x[3], x[2], x[1]))
print(li[-1][0])
print(li[0][0])

# N 찍기
n = int(input())

for _ in range