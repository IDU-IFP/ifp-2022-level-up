# 12933번 정수 내림차순으로 배치하기(프로그래머스)
def solution(n):
    ls = list(str(int(n)))
    ls.sort(reverse = True)
    return int("".join(ls))