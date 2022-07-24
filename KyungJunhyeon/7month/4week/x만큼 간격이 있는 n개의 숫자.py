def solution(x, n):
    if x > 0:
        answer = [i for i in range(x, x*n+1, x)]
    elif x == 0:
        answer = [0 for i in range(n)]
    else:
        x = -x
        answer = [-i for i in range(x, x*n+1, x)]
    return answer


if __name__ == "__main__":
    print(solution(2, 5))
