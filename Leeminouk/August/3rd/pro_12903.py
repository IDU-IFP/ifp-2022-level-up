def solution(s):
    is_even = len(s) % 2
    mid = int(len(s) / 2)
    
    if is_even == 0:
        answer = s[mid - 1:mid + 1]
    else:
        answer = s[mid:mid + 1]
    return answer