# 옵션에 따른 자동차 구매 액수 계산
"""
    입력 : 첫째 줄에 테스트 케이스 개수가 주어짐
        각 테스트 케이스의 첫 줄엔 자동차 가격 s 가 주어짐 (1 <= s <= 100,000)
            둘째 줄엔 해빈이가 구매하려는 서로 다른 옵션의 개수 n이 주어짐. (0 <= n <= 1000)
                총 n개의 줄이 입력. q, p로 이루어짐. 
                q는 사려는 특정 옵션의 개수 ( 1 <= q <= 100)
                p는 옵션의 가격 (1 <= p <= 10000)
    출력 : 각 테스트 케이스별 구매하려는 자동차 가격 출력
"""
def carController():
    typed = int(input())
    car_price = 0
    total_option = 0
    total_price = []

    for _ in range(typed):

        car_price = int(input())
        car_option = int(input())

        total_option = carOptionController(car_option)

        car_price += total_option

        total_price.append(car_price)

    carPricePrint(total_price)

def carOptionController(car_option):
    total_option = 0

    if car_option > 0:

            for _ in range(car_option):
                typed = input().split(" ")
                total_option += optionPriceCalculate(typed)

            return total_option

    else:
        return total_option

def optionPriceCalculate(option_info):
    return int(option_info[0]) * int(option_info[1])

def carPricePrint(car_price):
    for a in car_price:
        print(a)


carController()