#https: // www.acmicpc.net/problem/10950

count = int(input())
add = []
for i in range(count):
    a, b = map(int, input().split())
    add.append(a+b)
for j in range(count):
    print(add[j])
