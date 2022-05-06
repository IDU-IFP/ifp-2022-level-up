# 윷놀이

for _ in range(3):
    yut = input().split(" ") # 네 개의 윷짝의 결과 저장
    res = yut.count('0') # 윷짝 중 0의 개수 카운트

    if(res == 1): # 1개면 도
        print('A')
    elif(res == 2): # 2개면 개
        print('B')
    elif(res == 3): # 3개면 걸
        print('C')
    elif(res == 4): # 4개면 윷
        print('D')
    else: # 0 값이 없다면 모
        print('E')