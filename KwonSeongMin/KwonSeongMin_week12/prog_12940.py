#https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    l = n*m
    while m:
        n,m = m,n%m
        print(n, m)
    return [n,l//n]