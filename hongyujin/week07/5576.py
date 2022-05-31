W = []
K = []

for _ in range(10):  # W 대학
    W.append(int(input()))
for _ in range(10):  # K 대학
    K.append(int(input()))

W_top3 = sum(sorted(W, reverse=True)[0:3])  # 득점 높은 3명
K_top3 = sum(sorted(K, reverse=True)[0:3])

print(W_top3, K_top3)
