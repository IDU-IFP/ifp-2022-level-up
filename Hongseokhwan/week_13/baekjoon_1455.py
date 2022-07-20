# 뒤집기 2

n,m = map(int, input().split()) # 가로, 세로
arr = [] # 뒤집힌 동전을 저장할 배열
count = 0 # 뒤집은 횟수
table = str.maketrans("10", "01") # 0은 1로, 1은 0으로

for i in range(n): # 세로줄만큼 동전 입력
    arr.append(input())
 
for i in range(m-1,-1,-1): # 시작점에서 가장 먼곳부터 반복
  for j in range(n-1,-1,-1):
    if(arr[j][i] == "1"): # 뒷면이면
        count += 1 # 뒤집기 횟수 추가
        temp = j
        while (temp>=0): # 해당 범위에 포함되는 동전 다 뒤집기
            s = str(arr[temp][0:i+1])
            arr[temp] = s.translate(table)
            temp -= 1
print(count) # 횟수 출력