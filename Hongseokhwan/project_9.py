# 별찍기 - 4

# 출력할 줄 개수 입력
N = int(input())

# 공백은 0개부터 N-1개까지, 별은 N개부터 1개까지 순차적으로 출력
for i in range(N):
    print(' '*i+'*'*(N-i))