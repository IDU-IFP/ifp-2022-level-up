# 검증수

num_arr = map(int, input().split(" ")) # 고유번호 5자리 입력
res = 0 # 검증키를 담을 변수 선언

# 5자리 숫자를 제곱하여 덧셈
for num in num_arr:
    res += num**2

# 각 숫자를 제곱한 수들의 합을 10으로 나눈 나머지 출력(=검증키)
print(res % 10)

