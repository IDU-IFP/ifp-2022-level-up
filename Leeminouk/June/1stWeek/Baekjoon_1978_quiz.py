# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

import math

def primeNumber(factor, number):
    if factor > 1:
        if number % factor:
            return primeNumber(factor - 1, number)
        else:
            return False
    else:
        return True

def checkPrime():
    input()
    count = 0
    for i in map(int, input().split()):
        if i != 1:
            if primeNumber(int(math.sqrt(i)), i):
                count += 1

    return count

print(checkPrime())