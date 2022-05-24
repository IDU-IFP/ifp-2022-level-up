# 대회 자리

# 입력한 테스트 케이스만큼 반복. 참가자 수, 자리 수, 참가자별 원하는 자리를 입력
for _ in range(int(input())):
    want_seat = []
    player, seat = map(int, input().split())
    for _ in range(player):
        want_seat.append(input())
    
    # 중복되는 자리를 찾아 앉는 못하는 사람 수 출력
    print(player - len(set(want_seat)))