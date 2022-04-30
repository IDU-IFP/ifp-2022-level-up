# 별 찍기 - 20

n = int(input()) # 줄의 개수 입력

# 홀수 행은 '공백+별', 짝수 행은 '별+공백' 출력
for i in range(1, n+1):
    if(i % 2 == 0):
        print((" " + "*") * n)
    else:
        print(("*" + " ") * n)