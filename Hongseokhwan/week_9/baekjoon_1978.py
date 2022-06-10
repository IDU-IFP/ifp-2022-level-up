# 소수 찾기

n = int(input()) # 숫자 개수 입력
nums = list(map(int, input().split())) # 숫자 입력
res = 0 # 소수의 개수를 담을 변수

# 소수 판별
for num in nums:
    if(num == 1): # 1은 소수가 아니므로 제외
        continue

    count = 2 # 나누는 수

    # 나머지가 없으면 소수가 아니므로 while문 탈출
    while(num%count or num == count):
        if(num == count):
            res += 1
            break

        count += 1

# 소수의 개수 출력
print(res)