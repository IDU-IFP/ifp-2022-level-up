#  정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때 A에서 x 보다 작은 수를 모두 출력
"""
    입력 : 첫째 줄 N, X (1 <= N, X <= 10000)
            둘째 줄에는 수열 A를 이루는 정수 N개 
            주어지는 정수는 모두 1보다 크고 10000보다 작거나 같은 정수
    출력 : X 보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력. X보다 작은 수는 적어도 하나 존재
"""
import sys
number_a, find_x = [int(a) for a in sys.stdin.readline().split()]
typed = [int(a) for a in sys.stdin.readline().split()]
result = ""

for a in typed:
    if a < find_x:
        result += (str(a) + " ")

print(result)