# 12932번 자연수 뒤집어 배열로 만들기(프로그래머스)
def solution(n):
    a = []
    s = reversed(str(n))
    for i in s:
        a.append(int(i))
    return a