# 소수

m = int(input())
n = int(input())
arr = [i for i in range(m, n+1)] # m이상 n이하의 수로 이루어진 배열
sum = 0 # 소수의 합
r = int(n ** 0.5) # n의 제곱근

# 1은 소수가 아니므로 1 제거
if(arr.count(1)):
    arr.remove(1)

# 소수가 아닌 수들 제거
for i in range(2,r+1):
    for j in range(i+i,n+1,i):
        if (arr.count(j)):
            arr.remove(j)

# 소수의 합
for i in arr:
    sum += i

# 소수가 없으면 -1을, 있으면 합과 최솟값 출력
if(len(arr) == 0):
    print(-1)
else:
    print(sum)
    print(min(arr))

