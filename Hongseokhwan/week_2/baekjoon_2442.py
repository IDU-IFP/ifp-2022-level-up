# 별 찍기 - 5

n = int(input() ) # 줄 개수 입력

# 첫째 줄에는 별 1개 ... N번째 줄에는 별 2×N-1개 출력
for i in range(1,n+1):
    print(" " * (n-i) + "*" * (2*i-1))