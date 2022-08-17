# 문자열 다루기 기본

def solution(s):
    if(len(s)==4 or len(s)==6): # 문자열 길이가 4 혹은 6일 경우
        for w in s:
            if(w.isalpha()): # 문자열에 문자가 포함될 경우 False 반환
                return False

        return True
    else: # 문자열 길이가 4 혹은 6이 아닐경우 False 반혼
        return False