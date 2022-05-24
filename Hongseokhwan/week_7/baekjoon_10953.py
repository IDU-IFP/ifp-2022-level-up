# A+B - 6

# 테스트 케이스 수 만큼 반복, a 와 b 값을 입력받아 합한 값을 출력
for i in range(int(input())):
    a, b = map(int,input().split(','))
    print(a+b)