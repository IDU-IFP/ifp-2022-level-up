# 피보나치 수 5

arr = [] # 수를 담을 배열

# 0번째는 0, 1번째는 1, n번째는 n-2번째 수 + n-1변째 수의 합
for i in range(int(input())+1):
    if(i == 0):
        arr.append(0)
    elif(i == 1):
        arr.append(1)
    else:
        arr.append(arr[i-2]+arr[i-1])

# 베열의 마지막 수 출력
print(arr[-1])