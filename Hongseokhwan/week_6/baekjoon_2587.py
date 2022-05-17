# 대표값2

arr = [] # 자연수를 담을 배열

# 5개의 자연수 입력
for _ in range(5):
    arr.append(int(input()))

# 오름차순 정렬 후 평균값과 중앙값 출력
print(sum(arr)//5)
print((sorted(arr))[2])