sosu = [0 for i in range(10001)]
sosu[1] = 1
for i in range(2, 100):    # i가 2일 때
    for j in range(i * 2, 10001, i):  # 4를 기준으로 했을 때 4 ~ 10000까지 (소수가 아닌 수에 1로 채움)
        sosu[j] = 1                   # 값을 다 1로 채움 (0이나 아니나 판단하기 위해)
t = int(input())
for i in range(t):
    a = int(input())   # 내가 원하는 값을 받음 (8)
    b = a // 2         # 8을 2로 나눔 b = 4
    for j in range(b, 1, -1):   # 4 ~ 1까지 -1됨
        if sosu[a - j] == 0 and sosu[j] == 0:   # 8 - 3 = [5] 는 0이고 [3] = 0이면
            print(j, a - j)                     # (3, 5)
            break
