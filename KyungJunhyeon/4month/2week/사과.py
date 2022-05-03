count = 0
for i in range(int(input())):
    studentNum, appleNum = map(int, input().split())
    count += appleNum % studentNum
print(count)
