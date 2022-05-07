# x 보다 작은 수

n, x = map(int, input().split(" ")) # 수열의 요소 개수와 x 값 입력
num_arr = map(int, input().split(" ")) # 수열 요소 n개를 입력

# x 보다 작은 수들을 줄바꿈 없이 출력
for num in num_arr:
    if(num < x):
        print(num, end=" ")
