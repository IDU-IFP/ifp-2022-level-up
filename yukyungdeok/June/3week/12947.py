# 12947번 하샤드 수(프로그래머스)
def solution(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    if x%sum == 0:
        return True
    else:
        return False