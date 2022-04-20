# 별 찍기 - 8

n = int(input()) # n 값 입력

# 첫째 줄부터 2×N-1번째 줄까지 규칙에 맞춰 차례대로 별을 출력
for i in range(1,2*n):
    if(i <= n):
        print("*" * i+" " * (2*(n-i)) +"*" * i)
    else:
        print("*" * (2*n-i) + " " * (2*(i-n)) + "*" * (2*n-i))