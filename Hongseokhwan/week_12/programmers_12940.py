# 최대공약수와 최소공배수

def solution(n, m):
    f_answer = 1 # 최대공약수
    
    # 두 수의 최대공약수 구하기
    for i in range(2,min([n,m])+1):
        if(not(n % i) and not(m % i)):
            f_answer = i

    # 최소공배수 -> 두수를 최대공약수로 나눈 몫들과 최대공약수를 곱하기
    return [f_answer, f_answer * (n//f_answer) * (m//f_answer)]