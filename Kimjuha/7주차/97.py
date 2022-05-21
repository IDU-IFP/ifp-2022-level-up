baduk = []
for _ in range(19):
    baduk.append(list(map(int, input().split())))

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(19):
        baduk[i][y-1] = 1 if baduk[i][y-1] == 0 else 0
        baduk[x-1][i] = 1 if baduk[x-1][i] == 0 else 0


for b in baduk:
    print(*b)
