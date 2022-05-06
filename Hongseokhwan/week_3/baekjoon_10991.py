# 별 찍기 - 16

n = int(input()) # 줄의 개수 입력

# 공백 (n-1)개 ~ 0개 + '* ' 1개 ~ n개 까지 출력
for i in range(1, n+1):
    print((n - i) * " " + "* " * i)