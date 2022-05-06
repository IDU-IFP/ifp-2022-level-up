T = int(input())

for _ in range(T):
    n, a = input().split()   # n, a = (숫자, 문자열)
    n = int(n)               # n은 숫자여서 int로 바꿔줌
    print(a[:n-1] + a[n:])   # n을 기준으로 문자열을 나눈 후 합하여 출력
