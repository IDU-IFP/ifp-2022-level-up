a, m, d, n = map(int, input().split())

i = a
prog = []
while len(prog) < n:
    prog.append(i)
    i = i*m+d
print(prog[-1])
