# 문제
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

# 출력
# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

import math
number = int(input())
result = []

if number > 1:
    for i in range(2, number):
        
        while number % i == 0:
            number = int(number / i)
            result.append(i)

    if len(result) > 1:
        for a in result:
            print(a)

    else:
        print(number)

# n = int(input())

# if n != 1:
#     prime = [True] * (n + 1)
#     prime[0], prime[1] = False, False

#     k = n
#     for i in range(2, n + 1):
#         if prime[i]:
#             for j in range(i * i, n + 1, i):
#                 prime[j] = False

#             while k % i == 0:
#                 print(i)
#                 k = int(k / i)

#             if k == i:
#                 break