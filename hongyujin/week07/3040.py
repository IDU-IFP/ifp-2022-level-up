n = [int(input()) for _ in range(9)]  # 9명 난쟁이 모자 수 출력
hap = sum(n)   # 9명 난쟁이 모자 숫자 합

for i in range(9):    # 아닌 난쟁이 한명 빼기
    hap -= n[i]
    for j in range(i + 1, 9):  # 2명 중 나머지 난쟁이 빼기
        hap -= n[j]
        if hap == 100:
            n.remove(n[j])
            n.remove(n[i])
            break
        hap += n[j]
    else:
        hap += n[i]
        continue
    break
print(*n, sep=" \n")
