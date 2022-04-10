# 별찍기 - 2

# 출력할 줄 개수 입력
N = int(input())

# 공백은 N-1개부터 0개까지, 별은 1개부터 N개까지 순차적으로 출력
for i in range(1, N+1):
    print(' '*(N-i)+'*'*i)