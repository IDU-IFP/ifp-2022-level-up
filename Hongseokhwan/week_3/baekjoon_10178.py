# 할로윈의 사탕

t = int(input()) # 테스트 케이스 개수 입력

# 각 테스트 케이스마다 사탕의 개수와 형제의 수 입력 후 형제 한명당 받을 수 있는 사탕의 개수와 아버지에게 남는 사탕의 개수 출력
for _ in range(t):
    c,v = map(int, input().split(" "))
    print("You get {} piece(s) and your dad gets {} piece(s).".format(c//v, c%v))
