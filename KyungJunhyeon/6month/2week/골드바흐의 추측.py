# import math
# import sys


# def is_prime_number(x):
#     # 2부터 x의 제곱근까지의 모든 수를 확인하며
#     for i in range(2, int(math.sqrt(x)) + 1):
#         # x가 해당 수로 나누어떨어진다면
#         if x % i == 0:
#             return False  # 소수가 아님
#     return True  # 소수임


# makeList = []
# for i in range(4, 10000):
#     if is_prime_number(i) == True and i != 1:
#         makeList.append(i)

# for _ in range(int(input())):
#     number = int(sys.stdin.readline())
#     count = 1
#     for i in range(len(makeList)+1):
#         if makeList[i]*2 == number:
#             print(makeList[i], makeList[i])
#         elif i != len(makeList):
#             while(1):
#                 if i + count != len(makeList):
#                     if makeList[i] + makeList[i + count] == number:
#                         print(makeList[i], makeList[i+count])
#                         break
#                     count += 1
#                 else:
#                     break


#위 방식대로 풀다가 죽어도 안풀릴거같아서 인터넷 참고함..

#참고 https://yoonsang-it.tistory.com/31

def Goldbach():
    check = [False, False] + [True] * 10000
    
    for i in range(2, 101):
        if check[i] == True:
            for j in range(i + i, 10001, i):
                check[j] = False

    T = int(input())
    for _ in range(T):
        n = int(input())

        A = n // 2
        B = A
        for _ in range(10000):
            if check[A] and check[B]:
                print(A, B)
                break
            A -= 1
            B += 1

Goldbach()

#나중에 다시 손봐야지...ㅠㅠ