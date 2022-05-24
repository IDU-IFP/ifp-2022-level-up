# 5576번 콘테스트
w = []
k = []
for _ in range(10):
    w.append(int(input()))
for _ in range(10):
    k.append(int(input()))
w.sort(reverse=True)
k.sort(reverse=True)
wsum = 0
ksum = 0
for i in range(0, 3):
    wsum += w[i]
    ksum += k[i]
print(wsum, ksum)