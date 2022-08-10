from itertools import combinations
import copy
import sys
input = sys.stdin.readline

N = int(input())
space, teach, empty = [], [], []
is_hide = False

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
    tmp = list(input().split())
    space.append(tmp)

    for a, b in enumerate(tmp):
        if b == "T":
            teach.append((i, a))
        if b == "X":
            empty.append((i, a))

for set in combinations(empty, 3):
    graph = copy.deepcopy(space)

    for i in set:
        x, y = i
        graph[x][y] = "O"
    
    for i in teach:

        is_fail = [False] * 4
        for j in range(4):
            x, y = i

            while True:
                x += dx[j]
                y += dy[j]

                if x < 0 or x >= N or y < 0 or y >= N:
                    is_fail[j] = False
                    break

                if graph[x][y] == "O":
                    is_fail[j] = False
                    break
                if graph[x][y] == "S":
                    is_fail[j] = True
                    break
                else:
                    graph[x][y] = "T"
                
            if is_fail[j]:
                break

        if True in is_fail:
            is_hide = False
            break
        else:
            is_hide = True

    if is_hide:
        break

if is_hide:
    print("YES")
else:
    print("NO")
