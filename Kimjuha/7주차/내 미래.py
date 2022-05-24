# 훈련병인 철수는 교관의 지시에 따라야 한다.
# 교관은 "좌로 1보, 하로 2보 가!"와 같이 상,하,좌,우로 이동할 것을 명령한다.
# 철수의 현재 위치가 입력으로 주어질 때 교관의 명령대로 이동한 위치는 어디일까?
# 훈련소의 전체 공간 크기는 5 * 5이다.


x, y = map(int, input().split())
moves = list(map(int, input().split()))  # 좌 우 상 하 순서

result = [[0 for _ in range(5)]for _ in range(5)]
result[x-1+moves[3]-moves[2]][y-1+moves[1]-moves[0]] = 1

for i in result:
    print(*i)
