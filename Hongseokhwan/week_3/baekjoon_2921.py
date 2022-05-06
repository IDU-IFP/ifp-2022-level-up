# 도미노

n = int(input()) # 도미노 세트의 크기 입력
res = 0 # 결과를 담을 변수 선언

# 크기가 n인 도미노 세트의 점 개수 구하기
for i in range(n+1):
    num = i
    while(num <= n):
        res += i + num
        num += 1

# 점 개수 출력
print(res)