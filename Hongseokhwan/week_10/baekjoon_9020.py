# 골드바흐의 추측

import sys

n = []

# 배열에 정수 저장하기
for i in range(int(sys.stdin.readline())):
    n.append(int(sys.stdin.readline()))

# 입력한 정수 중 가장 큰 값의 소수를 찾고 배열로 생성
num_arr = [True] * max(n)
for i in range(2,int(max(n) ** 0.5)+1):
    if(num_arr[i-1] == True):
        for j in range(i+i, max(n), i):
            num_arr[j-1] = False
    
num_arr = [i for i in range(2, max(n)) if num_arr[i-1] == True]

# 정수의 중간 값부터 1씩 증감하면서 최소 간격의 소수를 찾은 후 출력
for i in n:
    y, z = i//2, i//2
    while(1):
        if(num_arr.count(y) and num_arr.count(z)):
            print(y, z)
            break
        else:
            y = y - 1
            z = z + 1