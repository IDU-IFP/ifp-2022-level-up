# 더하기

t = int(input()) # 테스트 케이스의 개수 입력

# 자연수 개수 n과 n개의 자연수를 입력 후 총합 출력
for _ in range(t):
    n = int(input())
    num_arr = map(int,input().split(" "))

    print(sum(num_arr))