# 새학기를 맞아 산 책 10권의 가격 확인. 10권 중 9권 가격만 확인 가능. 1권의 가격은?
"""
    입력 : 첫째 줄에는 10권의 총 가격.
        둘째 줄부터 9개의 줄에는 가격을 읽을 수 있는 책 9권의 가격이 주어짐. 책의 가격은 10000 이하의 양의 정수
    출력 : 첫쨰 줄에 가격을 읽을 수 없는 책의 가격을 출력
"""
TOTAL_BOOKS = 9
typed = int(input())


def unKnownPrice(typed):
    global TOTAL_BOOKS
    total_price = typed

    for _ in range(TOTAL_BOOKS):
        total_price -= int(input())

    return total_price


print(unKnownPrice(typed))