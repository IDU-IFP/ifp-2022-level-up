score = []   # 점수를 선언 (리스트)

for _ in range(5):    # for문을 5번 돌려서 점수들을 각 더하고 score에 추가 (append)
    score.append(sum(map(int, input().split())))

# score.index(max(score))+1 은 우승자의 번호, max(score)은 얻은 점수 출력
print(score.index(max(score))+1, max(score))
