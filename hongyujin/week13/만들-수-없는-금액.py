n = int(input())
coin = list(map(int, input().split()))
coin.sort()  # 화폐를 오름차순으로 정렬

target = 1
for i in coin:
    if target < i:  # 만들 수 없는 금액을 찾으면 반복 종료
        break
    target += i
print(target)
