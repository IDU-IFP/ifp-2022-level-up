t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    floor = n % h      # 손님이 10명일 때 6층 10 % 6은 4 그러므로 10번 째 손님은 402호
    room_num = (n//h) + 1  # 엘레베이터에서 떨어진 곳
    if floor == 0:   # 나머지가 0일 때
        floor = h
        room_num -= 1
    print(floor * 100 + room_num)
