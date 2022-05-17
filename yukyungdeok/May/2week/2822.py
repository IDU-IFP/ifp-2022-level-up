# 2822번 점수계산
score = []
for _ in range(8):
    score.append(int(input()))
temp = []
answer = 0
for _ in range(5):
    answer += max(score)
    temp.append(score.index(max(score)) + 1)
    score[score.index(max(score))] = -1
temp.sort()
print(answer)
print(*temp)