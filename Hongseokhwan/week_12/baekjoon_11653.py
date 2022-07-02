# 소인수분해

n = int(input()) # 숫자 입력
count = 2 # 나눌 숫자

# 1이면 아무것도 출력하지 않음
if(n == 1):
    print()
# 1이 아니면 1이 될때까지 소인수 분해
# 작은수부터 순차적으로 올라가기 때문에 소수로 나눗셈 될 수 밖에 없음
else:
    while(n != 1):
        if(n % count == 0):
            print(count) # 소인수 분해 과정 출력
            n = n // count
            count = 2
            continue
        else:
            count += 1
