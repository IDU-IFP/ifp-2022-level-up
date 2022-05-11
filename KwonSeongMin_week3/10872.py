#https://www.acmicpc.net/problem/10872
# n = 1
# for i in range(int(input())):
#     n *= (i+1)
# print(n)

#재귀함수 연습
#factorial(6) 6 * 5 * 4 * 3 * 2 * 1

def factorial(x):
    
    if x==1:
        return x
    else:
        return x * factorial(x-1)

print(factorial(int(input())))
# 백준에 기입시 RecursionError issue로 실행 안될거임.
# import sys   sys.setrecursionlimit(10**6) 붙이면 실행 됨.
