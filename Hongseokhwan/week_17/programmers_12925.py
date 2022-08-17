# 문자열을 정수로 바꾸기

def solution(s):
    if(s[0] == '-'): # 부호가 - 면
        return 0-int(s[1:]) # 부호 제외한 값을 0에서 뺀 후 리턴
    elif(s[0] == '+'): # 부호가 + 먄
        return int(s[1:]) # 부호 제외한 후 리턴
    else: # 부호가 없으면
        return int(s[0:]) # 그대로 리턴