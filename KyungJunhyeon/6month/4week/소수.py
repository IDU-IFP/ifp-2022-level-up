import math

listOfNumbers = []


def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


A = int(input())
B = int(input())

for i in range(A, B+1):
    if is_prime_number(i) == True and i != 1:
        listOfNumbers.append(i)


if len(listOfNumbers) >= 1:
    print(sum(listOfNumbers))
    print(min(listOfNumbers))
else:
    print(-1)
