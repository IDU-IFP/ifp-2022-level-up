# 제로

arr = [] # 정수를 담을 변수

# 입력받은 정수가 0일 경우 최근값 삭제, 0이 아닐경우 값 추가 
for _ in range(int(input())):
    n = int(input())
    if(n == 0):
        del arr[len(arr)-1]
    else:
        arr.append(n)

# 총합 출력
print(sum(arr))
