def solution(arr):
    t = ''
    answer = []
    
    for a in arr:
        if a != t:
            t = a
            answer.append(a)
    
    return answer