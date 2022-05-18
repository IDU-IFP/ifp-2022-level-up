# 짝수를 찾아라

# 테스트 케이스 만큼 반복, 정수를 입력 받아 짝수의 합과 짝수의 최솟값 구하고 출력
for i in range(int(input())):
    num_arr = list(map(int, input().split()))
    sum = 0
    min = max(num_arr)

    for num in num_arr:
        if(num % 2 == 0):
            sum += num
            if(min > num):
                min = num


    print(sum, min)
