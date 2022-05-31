def solution(x, n):
    answer = []
    num = x                # x를 num에 삽입
    for i in range(n):     # n번 반복
        answer.append(num)  # num값을 answer에 추가한다
        num += x           # num값에 x를 계속을 더한다
    return answer
