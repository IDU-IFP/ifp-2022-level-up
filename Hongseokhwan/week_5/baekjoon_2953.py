# 나는 요리사다

res_score = 0 # 우승자의 점수를 담을 변수 선언
res_num = 0 # 우승자의 번호를 담을 변수 선언

# 높은 점수를 받은 사람의 참가번호와 점수를 저장
for i in range(1,6):
    score = map(int, input().split(" "))
    total = sum(score)
    if(res_score < total):
        res_num = i
        res_score = total

# 우승자 번호와 점수를 출력
print(res_num, end=" ")
print(res_score)
    