def solution(seoul):
    dic = {b : a for a, b in enumerate(seoul)}
    return "김서방은 {}에 있다".format(dic["Kim"])