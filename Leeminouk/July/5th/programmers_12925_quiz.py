def solution(s):
    if s[0] == "-":
        return int("".join(list(s)[1:])) * -1
    else:
        return int(s)