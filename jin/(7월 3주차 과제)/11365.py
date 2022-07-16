N = True
while N:
    A = input()
    if A == "END":
        N = False
    else:
        print(A[::-1])