n = int(input())

for i in range(1, n + 1):  # 배열을 이용 1 ~ (n + 1) -1 까지
    print("*" * i)
for i in range((n - 1), 0, -1):
    print("*" * i)
