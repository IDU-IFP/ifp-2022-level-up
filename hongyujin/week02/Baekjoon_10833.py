n = int(input())  # 학교의 수
hap = 0

for _ in range(n):
    x, y = map(int, input().split())
    hap += y % x  # 남는 사과의 총 개수 구하기

print(hap)
