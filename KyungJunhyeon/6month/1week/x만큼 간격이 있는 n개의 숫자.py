# def solution(x, n):
#     if x >= 0:
#         answer = [i for i in range(x, x*n+1, x)]
#     else:
#         x = abs(x)
#         answer = [-i for i in range(x, x*n+1, x)]
#     return answer

# 꼼수가 실패했다... 정석적으로 풀이해야지.


def solution(x, n):
    if x > 0:
        answer = [i for i in range(x, x*n+1, x)]
    elif x == 0:
        answer = [0 for i in range(n)]
    else:
        x = -x
        answer = [-i for i in range(x, x*n+1, x)]
    return answer

# 깐깐하게 조건처리를 해야한다는점.. 흠.........
