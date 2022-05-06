# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램
"""
    입력 : 첫째 줄 n (1 <= n <= 10000)
    출력 : 1 부터 n까지의 합
"""
typed = int(input())
sum = 0

for a in range(1, typed+1):
    sum += a

print(sum)