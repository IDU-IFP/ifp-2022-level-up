n = int(input())
n1 = list(map(int, input().split()))

# 가장 작은 값과 가장 큰 값을 곱해야 진짜 수 구할 수 있다
n1_max = max(n1)
n1_min = min(n1)
print(n1_max * n1_min)
