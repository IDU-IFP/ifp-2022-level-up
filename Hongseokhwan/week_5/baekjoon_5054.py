# 주차의 신

t = int(input()) # 테스트 케이스의 개수

# 다녀갈 상점의 시작 위치와 끝 위치의 중앙에 주차 후 상점을 갔다 온 거리(=최소거리)를 출력
for _ in range(t):
    v = 0 
    n = int(input())
    arr = sorted(map(int, input().split()))
    parking_lot = (arr[0] + arr[n-1]) // 2

    for i in range(len(arr)):
        if(i == 0):
            v += parking_lot - arr[i]
        else:
            v += arr[i] - arr[i-1]
            if(i == len(arr) - 1):
                v += arr[i] - parking_lot
    print(v)


