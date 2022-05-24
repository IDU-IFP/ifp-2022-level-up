#https://www.acmicpc.net/problem/9085
#10보다 작거나 같은 자연수 N개를 주면 합을 구하는 프로그램을 작성하시오.

test_case = int(input())
for i in range(test_case):
    n = int(input())
    num = list(map(int, input().split()))
    print(sum(num))
