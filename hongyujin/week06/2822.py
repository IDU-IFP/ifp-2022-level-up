score = []
temp = []
answer = 0
for i in range(8):    # 점수 8개를 입력
    score.append(int(input()))

for i in range(5):    # 가장 높은 점수 5개
    answer += max(score)
    temp.append(score.index(max(score)) + 1)
    score[score.index(max(score))] = -1
temp.sort()
print(answer)
print(*temp)
