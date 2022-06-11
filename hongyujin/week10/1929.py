x, y = map(int, input().split())

for i in range(x, y+1):
    if i == 1:    # 1은 소수가 아님
        continue
    for j in range(2, int(i ** 0.5)+1):  # 모든 수를 볼 필요 없음, 해당 수의 제곱근까지 보기
        if i % j == 0:
            break
    else:
        print(i)
