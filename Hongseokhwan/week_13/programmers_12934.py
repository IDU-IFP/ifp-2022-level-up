# 정수 제곱근 판별

def solution(n):
    res = int(n ** 0.5) # 제곱근 값을 정수형으로 변환
    answer = -1 # 제곱이 아닐 경우 -1 반환
    if(res ** 2 == n): # 입력받은 수와 res 제곱 값이 같다면
        answer = (res+1) ** 2 # res 에 1을 더한 후 제곱
    
    return answer