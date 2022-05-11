# 상수

num_1, num_2 = input().split(" ") # 두 수 입력

# 두 수를 뒤집어 비교가능한 정수로 형변환
num_1 = int(num_1[::-1])
num_2 = int(num_2[::-1])

# 비교해서 큰 수를 출력
if(num_1 > num_2):
    print(num_1)
else:
    print(num_2)