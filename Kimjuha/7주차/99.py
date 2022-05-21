ant_house = []
for i in range(5):
    matrix = list(map(int, input().split()))
    ant_house.append(matrix)


x, y = 1, 1
while ant_house[x][y] != 2:
    if ant_house[x][y] == 0:
        ant_house[x][y] = 9
        y += 1
    else:
        x += 1
        y -= 1
ant_house[x][y] = 9

for house in ant_house:
    print(*house)
