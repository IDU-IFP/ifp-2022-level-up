# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

starNum = int(input())
for i in range(1, starNum+1):
    for j in range(i):
        print("*", end="")
    print("")
