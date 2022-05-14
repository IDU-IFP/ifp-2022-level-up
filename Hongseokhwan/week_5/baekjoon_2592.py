# 대표값

num_arr = [] # 최빈값을 비교하기 위한 배열 선언
res = 0 # 최빈값을 구하기 위한 변수 선언
sum = 0 # 평균값을 구하기 위한 변수 선언

# 최빈값은 값이 배열에 없으면 그 값과 카운터 1 추가, 있으면 그 값의 카운터 + 1 하기
# 평균값은 입력하는 즉시 sum 변수에 덧셈
for _ in range(10):
    n = int(input())
    sum += n
    if(num_arr.count(n) == 0):
        num_arr.append(n)
        num_arr.append(1)
    else:
        num_arr[num_arr.index(n)+1] = num_arr[num_arr.index(n)+1] + 1

# 홀수 인덱스의 값(=카운터)을 비교하여 제일 큰 값 res 에 저장
for i in range(1,len(num_arr),2):
    if(res < num_arr[i]):
        res = num_arr[i]

sum = sum // 10 # 평균값 구하기
res = num_arr[num_arr.index(res)-1] # 최빈값 구하기

# 출력
print(sum)
print(res)

    