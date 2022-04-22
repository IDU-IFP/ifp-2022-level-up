import sys
n = int(sys.stdin.readline())  # 멀티탭의 개수
sum = 0  # 콘센트 꼽을 수 있는 개수

for _ in range(n):
    sum += int(sys.stdin.readline())

print(sum - (n - 1))
