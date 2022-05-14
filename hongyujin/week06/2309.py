n = []  # 난쟁이들 리스트에 선언
for i in range(9):   # 9번 반복
    n.append(int(input()))
hap = sum(n)  # 난쟁이들 총합 (키)
a = 0  # 다른 난쟁이 1 변수 선언
b = 0  # 다른 난쟁이 2 변수 선언

for i in range(8):
    for j in range(i+1, 9):
        if hap - (n[i] + n[j]) == 100:  # hap - (난쟁1 + 난쟁2) == 100
            a = n[i]
            b = n[j]
n.remove(a)
n.remove(b)
n.sort()    # 오름차순
for i in n:
    print(i)
