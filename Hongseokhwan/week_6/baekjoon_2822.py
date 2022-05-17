# 점수 계산

score_arr = [] # 점수를 담을 배열
num_arr = [] # 문제 번호를 담을 배열
sum = 0 # 최종 점수를 담을 변수

# 8문제의 점수 입력
for i in range(8):
    score_arr.append(int(input()))

test_arr = sorted(score_arr, reverse=True) # 점수 배열을 내림차순해서 새로운 배열 생성

# 가장 높은 5개의 점수를 더하고 점수 번호 저장 
for i in range(5):
    num_arr.append(score_arr.index(test_arr[i]))
    sum += score_arr[num_arr[i]]

    # 다 저장되면 점수 번호 오름차순 정리
    if(i == 4):
        num_arr.sort()

# 최종 점수 및 점수 번호 출력
print(sum)
for num in num_arr:
    print(num + 1, end=" ")
