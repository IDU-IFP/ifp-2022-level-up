n = int(input())  # 수의 개수
num = map(int, input().split())  # 수들
count = 0   # 소수 개수

for i in num:
    for j in range(2, i+1):  # 2부터 i 까지
        if i % j == 0:      # 나머지가 0이면 몫이 1
            if i == j:      # 나 자신을 찾기
                count += 1  # 개수 더해줌
            break
print(count)
