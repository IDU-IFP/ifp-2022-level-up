# 소수 구하기

import sys # 입력 시간 줄이기 위함

m, n = map(int, sys.stdin.readline().split()) # 정수 범위 입력

# 에라토스테네스의 체 이용
# n의 제곱근 이하의 수들의 배수만 지워 소수를 찾는 방법
num_arr = [True] * n 
last = int(n ** 0.5) # n의 제곱근

for i in range(2, last+1): # n의 제곱근 이하의 수 반복
    if(num_arr[i-1] == True):
        for j in range(i+i, n+1, i): # 배수들 지우는 과정
            num_arr[j-1] = False # 배수들은 False 값 저장

# 1을 제외한 True 값 출력
print(*[i for i in range(m, n+1) if (i != 1 and num_arr[i-1] == True)], sep="\n")