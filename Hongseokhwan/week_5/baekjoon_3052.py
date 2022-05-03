# 나머지

rest_arr = [] # 서로 다른 나머지를 담을 변수 선언

# 42 로 나눈 나머지가 배열에 없으면 추가, 있으면 추가 없이 반복문 진행
for _ in range(10):
    n = int(input())
    rest = n % 42

    if(not rest_arr.count(rest)):
        rest_arr.append(rest)

# 서로 다른 나머지의 개수 출력
print(len(rest_arr))