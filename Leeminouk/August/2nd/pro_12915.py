def solution(strings, n):
    temp = [a[n] for a in strings]
    result = []

    strings.sort()
    temp.sort()
    for i in temp:
        for j in strings:
            if i == j[n]:
                result.append(j)
                strings.remove(j)
                break

    return result
