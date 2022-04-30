# 주사위

t = int(input()) # 테스트 케이스의 개수 입력

# 각 테스트 케이스마다 주사위를 두 번 던져 나온 두 수를 입력 후 두 수의 합을 정해진 출력문에 맞게 출력
for i in range(1,t+1):
    x, y = map(int, input().split(" "))
    print("Case {}: {}".format(i, x+y))