#https://www.acmicpc.net/problem/5800

for t in range(int(input())):
    n = input().split()
    print("Class",t+1)
    arr = []
    m=0
    for i in range(1,len(n)):
        arr.append(int(n[i]))   # 첫 숫자 버리고 그 다음숫자부터 배열 삽입
    arr.sort()
    for i in range(1,len(arr)):
        if arr[i] - arr[i-1] > m:   # 격차가 큰 숫자를 찾는 과정
            m = arr[i] - arr[i-1]
        
    print("Max %d, Min %d, Largest gap %d" % (max(arr),min(arr),m))
