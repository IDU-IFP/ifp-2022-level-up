line, count = map(int, input().split())
linelist = list(map(int, input().split()))
for i in range(line):
    if linelist[i] < count:
        print(linelist[i], end=" ")
