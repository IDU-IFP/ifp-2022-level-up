#https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    i = 1
    while True: # 브루트포스 느낌
        if i*i == n:
            return (i+1) * (i+1)    
        elif i*i > n:   # 제곱근이 내가 입력한 수 보다 커지면 break 느낌
            return -1
        i += 1
