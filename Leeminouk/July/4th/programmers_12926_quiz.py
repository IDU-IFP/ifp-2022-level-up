def solution(s, n):
    result = []
    for i in s:
        if i != " ":
            if ord(i) > 96:
                if ord(i) + n > 122:
                    result.append(chr(ord(i) + n - 26))
                else:
                    result.append(chr(ord(i) + n))
            else:
                if ord(i) + n > 90:
                    result.append(chr(ord(i) + n - 26))
                else:
                    result.append(chr(ord(i) + n))
        else:
            result.append(i)
                                  
    return "".join(result)