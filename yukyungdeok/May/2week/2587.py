# 2587번 대표값2
n = []
for _ in range(5):
    n.append(int(input()))
n.sort()
print(int(sum(n)/5))
print(n[2])