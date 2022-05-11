# 오타맨 고창영

t = int(input()) # 테스트 케이스의 개수 입력
ch_arr = [] # 문자열을 담을 배열 선언

# 오타낸 위치와 문자열을 입력받은 후 오타낸 위치의 문자를 제외하고 출력
for i in range(t):
    n, s = input().split(" ")
    n = int(n)

    for i in range(len(s)):
        if(i+1 == n):
            continue
        else:
            print(s[i], end="")

    print()