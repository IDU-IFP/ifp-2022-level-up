# ACM 호텔

# 테스트 케이스만큼 반복
for _ in range(int(input())):
    h, w, n = map(int, input().split()) # 호텔의 높이, 너비, n번쨰 손님 입력
    h_count = 1 # YY
    w_count = 1 # XX
    
    # h를 n으로 나누었을 떄 몫은 XX, 나머지는 YY와 관련됨을 이용
    while(n//h):
        n -= h
        if(n): # n과 h가 동일해 발생하는 무의미한 덧셈을 제어
            w_count += 1

    h_count = n
    if(not n): # 나머지가 0이면 최고층이므로 h 저장
        h_count = h
    if(w_count < 10):
        print(str(h_count)+"0"+str(w_count))
    else:
        print(str(h_count)+str(w_count))