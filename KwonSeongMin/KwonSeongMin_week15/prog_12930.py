#https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    w = []
    count = 0
    for word in s:
        if word != ' ':
            if count % 2 == 0:
                w.append(word.upper())
            else:
                w.append(word.lower())
            count += 1
        else:
            count = 0
            w.append(' ')
    return ''.join(w)
