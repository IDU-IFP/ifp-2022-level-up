# 시저 암호

def solution(s, n):
    upper = [chr(i) for i in range(65, 91)] # 대문자
    lower = [chr(i) for i in range(97,123)] # 소문자
    answer = "" # 결과
    
    for w in s: # 입력한 문자 1개씩 반복
        if(w.isupper()): # 대문자라면
            i = upper.index(w) # 대문자 배열에서 해당 문자의 인덱스 추출
            answer += upper[(i+n) % 26] # n 만큼 민 후 추가
        elif(w.islower()): # 소문자라면
            i = lower.index(w) # 소문자 배열에서 해당 문자의 인덱스 추출
            answer += lower[(i+n) % 26] # n 만큼 민 후 추가
        else: # 공백이라면
            answer += w # 바로 추가
    
    return answer # 결과 출력