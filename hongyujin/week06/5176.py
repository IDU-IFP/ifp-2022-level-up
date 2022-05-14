k = int(input())

for i in range(k):
    p, m = list(int, input().split())
    data = [0] * (m + 1)       # 입력 받은 m+1을 0으로 초기화한다
    result = 0

    for i in range(p):
        seat = int(input())
        if data[seat] == 0:    # 원하는 자리 seat를 입력 받고 data 리스트의 seat가 0일 경우 앉기
            data[seat] = 1     # 1로 바꾸기
        else:
            result += 1        # 0이 아닐 경우 result를 1 증가
        print(result)
