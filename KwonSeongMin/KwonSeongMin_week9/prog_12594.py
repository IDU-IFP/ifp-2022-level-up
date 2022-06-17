#https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = []
    for i in range(1,n+1,1):
        answer.append(x*i)  #x*i 값 append
    return answer
