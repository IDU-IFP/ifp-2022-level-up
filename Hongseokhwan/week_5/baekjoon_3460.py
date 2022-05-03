# 이진수

t = int(input()) # 테스트 케이스의 개수

# 숫자 입력 후 이진수로 변환해 1의 위치를 출력
for i in range(t):
    n = int(input())
    n = str(bin(n))

    for i in range(len(n)-1,-1,-1):
        if(n[i] == "1"):
            print(len(n)-1-i, end=" ")
    
    print()
