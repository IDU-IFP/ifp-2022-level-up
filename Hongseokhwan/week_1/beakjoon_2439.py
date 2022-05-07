# 별 찍기 - 2

# 줄 개수 입력
N = int(input())

# N번째 줄에 별 N개를 오른쪽부터 출력
for i in range(1, N+1):
    print(' '*(N-i)+'*'*i)