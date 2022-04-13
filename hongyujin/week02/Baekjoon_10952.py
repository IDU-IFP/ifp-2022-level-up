while True:  # 참이면
    a, b = map(int, input().split())
    if a == 0 and b == 0:  # break문을 이용해 a, b = 0
        break
    else:
        print(a + b)  # 아니면 a + b를 출력한다
