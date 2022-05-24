# 10987번 모음의 개수
n = 0
for i in input():
    if i in ['a', 'e', 'i', 'o', 'u']:
        n += 1
print(n)