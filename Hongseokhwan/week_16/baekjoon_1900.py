# 레슬링
# 제일 강한 선수부터 차례대로 서야 최소의 금화를 사용할수 있다.

arr = [] # 결과

n = int(input()) # 레슬링 참여자 수

for i in range(n):
    arr.append(list(map(int, input().split()))) # 힘과 마술링
    arr[i].insert(0,i+1) # 레슬링 참여자 번호

for i in range(1, len(arr)): # 삽입 정렬 알고리즘으로 제일 강한 선수부터 정렬
    for j in range(i, 0 ,-1):
        if(arr[j][1]+(arr[j][2]*arr[j-1][1]) > arr[j-1][1]+(arr[j-1][2]*arr[j][1])):
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break

for i in range(n): # 레슬링 참여자 번호 출력
    print(arr[i][0])