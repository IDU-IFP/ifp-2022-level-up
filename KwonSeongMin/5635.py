# https://www.acmicpc.net/problem/5635
n = int(input())

name, birth, sorted_birth = [], [], []
for _ in range(n):
    file = input().split()
    name.append(file[0])
    birth.append([int(file[1]), int(file[2]), int(file[3])])

sorted_birth = sorted(birth, key=lambda x: (x[2], x[1], x[0]))

print(name[birth.index(sorted_birth[n-1])])
print(name[birth.index(sorted_birth[0])])
