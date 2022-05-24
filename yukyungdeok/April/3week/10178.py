# 10178번 할로윈의 사탕

for _ in range(int(input())):
    c, v = map(int, input().split())
    print("You get %d piece(s) and your dad gets %d piece(s)." %(c//v, c%v))