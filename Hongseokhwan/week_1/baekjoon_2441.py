# 별 찍기 - 4

# 줄 개수 입력
N = int(input())

# 첫째 줄에 별 N개, 둘째 줄에 별 N-1개 ... N번째 줄에 별 1개를 오른쪽부터 출력
for i in range(N):
    print(' '*i+'*'*(N-i))