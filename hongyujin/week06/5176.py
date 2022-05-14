k = int(input())

for _ in range(k):
    p, m = map(int, input().split())
    data = [0] * (m + 1)      # 입력 받은 m+1을 0으로 초기화한다
    count = 0

    for _ in range(p):
        seat = int(input())
        if data[seat] == 0:   # 원하는 자리 seat를 입력 받고 data 리스트의 seat가 0일 경우 앉기
            data[seat] = 1       # 1로 바꾸기
        else:
            count += 1            # 0이 아닐 경우 count를 1 증가한다

    print(count)
