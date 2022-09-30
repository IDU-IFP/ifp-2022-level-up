def solution(price, money, count):
    total = int(((count + 1) * count) / 2)
    if money - (total * price) < 0:
        answer = (money - (total * price)) * -1
    else:
        answer = 0

    return answer