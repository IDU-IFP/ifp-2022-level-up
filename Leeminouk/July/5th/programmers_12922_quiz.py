def solution(n):
    t = int(n / 2)
    if n % 2 == 0:
        return "수박" * t
    else:
        return "수박" * t + "수"