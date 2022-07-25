#https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    for word in s:
        if word != ' ':
            q = ord(word)+n
            if q > ord('Z') and word.isupper():
                q -= 26
            if q > ord('z') and word.islower():
                q -= 26
            answer += chr(q)
        else:
            answer += word
    return answer