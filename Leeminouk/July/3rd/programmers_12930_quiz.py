def solution(s):
    count = 0
    result = []
    for a in s:
        if a != " ":
            if count % 2 == 0:
                result.append(a.upper())
            else:
                result.append(a.lower())
            count += 1
        else:
            count = 0
            result.append(a)
    return "".join(result)