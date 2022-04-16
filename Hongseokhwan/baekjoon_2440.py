# 별 찍기 - 3

# 줄 개수 입력
N = int(input())

# 첫째 줄에 별 N개, 둘째 줄에 별 N-1개 ... N번째 줄에 별 1개 출력
for i in range(N):
    print('*'*(N-i))