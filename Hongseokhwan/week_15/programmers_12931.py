# 자릿수 더하기

def solution(n):
    answer = 0
    
    for w in str(n): # 문자열로 바꿔 각 자릿수 수를 더하기
        answer += int(w)
        
    return answer