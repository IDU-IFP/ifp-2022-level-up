# A+B - 3

t = int(input()) # 테스트 케이스의 개수 입력
a, b = [], [] # a, b 값을 저장할 배열 선언

# t 만큼 반복해 a, b 값을 입력
for i in range(0,t):
    num1, num2 = input().split(" ")
    a.append(int(num1))
    b.append(int(num2))

# 입력받은 a, b 값을 같은 인덱스끼리 더해 출력
for i in range(0,t):
    print(a[i]+b[i])