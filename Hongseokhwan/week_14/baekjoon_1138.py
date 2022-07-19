# 한 줄로 서기

n = int(input()) # 사람 수
arr = list(map(int, input().split())) # 자기보다 큰 사람 순서대로 담은 배열
num = [i for i in range(1,n+1)] # 키를 담을 배열
res = ["" for i in range(n)] # 결과
index = 0 # 인덱스

# 빈 자리에서부터 큰 사람 수 만큼 건너뛰고 줄 세우기
for i in range(len(num)):
    left = arr[i]
   
    while left:
        if(not res[index+1]):
            left -= 1
        index += 1
    res[index] = num[i]
    if('' in res):
        index = res.index('')

print(*res) # 결과 출력