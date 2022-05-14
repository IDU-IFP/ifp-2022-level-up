def goto(integer, i):
    if integer[i] == 0:
        return
    print(integer[i])
    i += 1
    goto(integer, i)


integer = list(map(int, input().split()))
goto(integer, 0)
