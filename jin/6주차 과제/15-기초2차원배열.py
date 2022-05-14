# 내 미래

cur = tuple(map(int, input().split()))
lf, rgt, up, down = map(int, input().split())
coords = [[0 for _ in range(5)] for _ in range(5)]

move = ( cur[0] -up +down, cur[1] -lf +rgt )
coords[move[0] -1][move[1] -1] = 1

for crd in coords:
  print( *crd )

# 바둑판에 흰 돌 놓기

import numpy as np
n = int(input())
baduk = np.zeros((19,19), dtype=int)
# baduk = [[0 for _ in range(19)] for _ in rnage(19)]

for _ in range(n):
  x, y = map(int, input().split())
  baduk[x-1][y-1] = 1

for bd in baduk:
  print(*bd)

# 바둑판에 십자 뒤집기

# 1. 초기 십자 바둑판 입력
baduk = []
for _ in range(19):
  matrix = list(map(int, input().split()))
  baduk.append(matrix)

# 2. n과 좌표 값을 입력받고 그에 따라 십자 형태에 맞춰 흑->백, 백->흑으로 변환
n = int(input())
for _ in range(n): # n번 입력
  x, y = map(int, input().split()) # x와 y 좌표 입력
  for i in range(19): # 변환
    baduk[i][y-1] = 1 if baduk[i][y-1] == 0 else 0 # 0->1, 1->0으로 변환
    baduk[x-1][i] = 1 if baduk[x-1][i] == 0 else 0 # 0->1, 1->0으로 변환

# 3. 변환된 값을 한 줄 단위로 출력
for i in range(19):
  print(*baduk[i])

# 설탕과자 뽑기

h, w = map(int, input().split())
shape = [[0 for _ in range(w)] for _ in range(h)]
n = int(input())

for _ in range(n) :
  l, d, x, y = map(int, input().split())
  x, y = x-1, y-1

  if d == 0 :
    for i in range(l) :
      shape[x][y+i] = 1
  else :
    for i in range(l) :
      shape[x+i][y] = 1

for s in shape :
  print( *s )

# 성실한 개미

ant_house = []
for i in range(5):
  matrix = list(map(int, input().split()))
  ant_house.append(matrix)

print('===================')

x, y = 1, 1
while ant_house[x][y] != 2:
  if ant_house[x][y] == 0:
    ant_house[x][y] = 9
    y += 1
  else:
    x += 1
    y -= 1
ant_house[x][y] = 9

for house in ant_house :
  print( *house )