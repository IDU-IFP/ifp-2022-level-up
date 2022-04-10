# 합

N = int(input()) # N 입력
sum = 0 # 합을 저장할 변수

# 1부터 N까지 반복하며 변수 sum 에 더하고 저장
for i in range(1,N+1):
    sum += i

# 1부터 N까지의 합 출력
print(sum)