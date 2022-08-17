def solution(s):
    t = list(s)
    if len(t) == 4 or len(t) == 6:
        for i in s:
            if ord(i) >= 65:
                return False
    else:
        return False

    return True