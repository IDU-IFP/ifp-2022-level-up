# 베르트랑 공준

import sys

while(True):
    n = int(sys.stdin.readline()) # 정수 입력
    if (n == 0): # 0일 경우 종료
        break
    elif(n == 1): # 1일 경우 무조건 출력 값은 1
        print(1)
        continue
    # n+1 부터 2n 범위에 있는 소수의 개수를 센 후 출력
    num_arr = [True] * (n*2)
    m = int((n*2) ** 0.5)

    for i in range(2, m+1):
        if(num_arr[i-1] == True):
            for j in range(i+i, n*2, i):
                num_arr[j-1] = False
    print(num_arr[n:].count(True)-1)