S = input()
alp = 'abcdefghijklmnopqrstuvwxyz'

for i in alp:      # 알파벳의 존재 유무 확인
    if i in S:
        print(S.index(i), end=' ')  # 존재하면 S위치 출력
    else:
        print(-1, end=' ')
