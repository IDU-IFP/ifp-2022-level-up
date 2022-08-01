def solution(p):
    u, v = [], []
    ul, ur = 0, 0
    is_same = False

    if not len(p):
        return ""

    else:
        for i in p:
            if not is_same:
                if i == "(":
                    ul += 1
                    u.append(i)

                else:
                    ur += 1
                    u.append(i)

                if ul == ur:
                    is_same = True

            else:
                v.append(i)

        if isCorBrac(u):
            return "".join(u) + solution(v)

        else:
            u.pop()
            u.pop(0)
            t = ""
            for i in u:
                if i == "(":
                    t += ")"
                else:
                    t += "("
            return "(" + solution(v) + ")" + t

def isCorBrac(u):
    is_correct = False
    t = []
    for a in u:
        if a == "(":
            t.append(a)
        if a == ")":
            try:
                t.pop()
            except:
                return is_correct

    if not len(t):
        is_correct = True

    return is_correct