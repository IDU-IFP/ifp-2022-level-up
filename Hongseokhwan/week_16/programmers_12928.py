# 약수의 합

def solution(n):
    answer = 0 # 결과
    for i in range(1,n+1): # 정수 n까지
        if(n % i == 0): # i 로 나눈 나머지가 0이면 n의약수
            answer += i 
    return answer # 결과값 리턴