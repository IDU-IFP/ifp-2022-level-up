s = input()

count0 = 0  # 모두 0으로 뒤집는 경우
count1 = 0  # 모두 1로 뒤집는 경우

if s[0] == '1':   # 첫 번째 원소 처리
    count0 += 1
else:
    count1 += 1

for i in range(1, len(s) - 1):  # 두 번째 원소부터 모든 원소 확인
    if s[i] != s[i + 1]:  # 다음 수에서 1로 바뀌는 경우
        if s[i + 1] == '1':
            count0 += 1
        else:           # 다음 수에서 0으로 바뀌는 경우
            count1 += 1

print(min(count0, count1))  # 더 적은 횟수를 가지는 경우 출력
