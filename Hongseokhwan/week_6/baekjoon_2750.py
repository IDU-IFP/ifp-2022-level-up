# 수 계산하기

num_arr = [] # 입력한 수를 담을 배열

# n 개의 수를 입력받아 배열에 저장
for _ in range(int(input())):
    num_arr.append(int(input()))

# 오름차순 정렬 후 출력
print(*sorted(num_arr), sep="\n")