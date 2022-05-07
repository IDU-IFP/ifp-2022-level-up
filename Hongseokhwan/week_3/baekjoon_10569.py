# 다면체

t = int(input()) # 테스트 케이스 개수 입력

# 테스트 케이스마다 꼭지점의 개수와 모서리의 개수를 입력 후 공식을 이용해 면의 개수를 출력
for i in range(t):
    v, e = map(int, input().split(" "))
    m = 2 - v + e
    print(m)