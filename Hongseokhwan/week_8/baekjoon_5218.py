# 알파벳 거리

# 테스트 케이스 만큼 반복.
# 두 단어를 입력 받아 한 문자씩 추출해 두 문자 사이의 거리를 출력
for _ in range(int(input())):
    x,y = input().split()
    print("Distances:", end=" ")
    for i in range(len(x)):
        if(y[i]>=x[i]):
            res = ord(y[i]) - ord(x[i])
        else:
            res = ord(y[i])+26 - ord(x[i])
        
        print(res, end=" ")
    
    print()