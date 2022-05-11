# 쉽게 푸는 문제

a, b = map(int, input().split(" ")) # 구간의 시작과 끝을 입력
res_arr = [] # 결과를 담을 배열 선언
count = 1 # 반복문의 step

# 구간의 끝까지 수열을 제작
for i in range(1,b+1,count):
    for _ in range(count):
        res_arr.append(count)
    count += 1

res_arr = res_arr[a-1:b] # 구간의 사직부터 구간의 끝까지 res_arr 배열에 저장
print(sum(res_arr)) # 구간에 속하는 숫자의 합 출력