#https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    k = x
    n = 0
    while x:
        n += x % 10
        x //= 10
    if k % n == 0:
        answer = True
    else:
        answer = False
    return answer
