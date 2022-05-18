# 동전 0

n, k =map(int, input().split()) # 돈의 단위 개수와 가격 입력
money_arr = [] # 돈을 단위별로 담을 배열
count = 0 # 필요한 최소 개수를 담을 변수

# 돈을 단위별로 입력
for _ in range(n):
    money_arr.append(int(input()))

money_arr.sort(reverse=True) # 내림차순으로 정렬

# 큰 수부터 가격에서 깎아 필요한 돈의 최소 개수 구하기
for money in money_arr:
    if(k // money >= 1):
        count += k // money
        k %= money
# 출력
print(count)