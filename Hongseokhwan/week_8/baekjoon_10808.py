# 알파벳 개수

arr = [0 for _ in range(26)] #  알파벳 개수

# 입력한 알파벳의 개수 카운트
for alpha in input():
    arr[ord(alpha)-97] += 1

# 출력
print(*arr)