def solution(n):
    n = str(n)
    answer = list(n)
    answer.sort(reverse=True)

    answer = ''.join(answer)
    answer = int(answer)
    return answer
