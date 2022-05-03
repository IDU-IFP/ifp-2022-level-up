n, x = map(int, input().split())
num = list(map(int, input().split()))  # n, x로 입력받고 num 변수에 숫자들을 list에 넣는다

for i in range(n):  # i는 0 ~ 9까지 입력 받기 (n이 10이여서)
    if num[i] < x:
        print(num[i], end=" ")
