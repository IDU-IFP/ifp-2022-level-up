# 이상한 문자 만들기

def solution(s):
    count = 0 # 글자 카운트
    answer = "" # 답안
    
    for w in s:
        if(w == " "): # 공백이면 문자열 결합 후 글자 카운트 초기화
            answer += w 
            count = 0
        else: # 문자일 때
            if(count % 2 == 0): # 짝수 번째라면 대문자
                answer += w.upper()
            else: # 홀수 번째라면 소문자
                answer += w.lower()
            count += 1
            
    return answer