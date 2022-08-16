def solution(a, b):
    if a == b:
        return a
    else:
        small, big = min(a, b) - 1, max(a, b)

        return int((big * (big + 1)) / 2) - int((small * (small + 1)) / 2)