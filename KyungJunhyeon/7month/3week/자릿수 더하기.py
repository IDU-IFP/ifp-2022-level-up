def solution(n):
    count = 0
    n = str(n)
    listN = list(n)
    for i in listN:
        count += int(i)
    return count


print(solution(123))
