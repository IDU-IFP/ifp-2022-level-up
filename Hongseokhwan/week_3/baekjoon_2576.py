# 홀수

num_arr = [] # 수를 담을 배열 선언
sum = 0 # 홀수의 총합을 담을 변수 선언

# 7개의 수 입력해 홀수만 배열에 저장
for _ in range(7):
    x = int(input())
    if(x % 2 != 0):
        num_arr.append(x)

# 홀수의 총합
for num in num_arr:
    sum += num

# 입력값 중 홀수가 없을 경우
if(sum == 0):
    print(-1)
# 홀수가 한개라도 존재할 경우
else:
    print(sum)
    print(min(num_arr))