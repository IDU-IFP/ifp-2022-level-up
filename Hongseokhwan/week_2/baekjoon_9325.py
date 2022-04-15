# 얼마?

t = int(input()) # 테스트 케이스의 개수 입력
res = [] # 테스트 케이스의 결과를 담을 배열 선언

# 각 테스트의 자동차 가격과 옵션의 개수와 가격 입력 후 저장
for _ in range(t):
    car_price = int(input())
    total = car_price
    n = int(input())
    for _ in range(n):
        option_count, option_price = map(int,input().split(" "))
        total += option_count * option_price

    res.append(total)

# 구입하려는 자동차의 가격을 차례대로 출력
for i in res:
    print(i)
