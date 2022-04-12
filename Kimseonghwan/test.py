if(1 and 0):
    print(0)
else:
    print(1)

typed_int = int(input())

for a in range(1, typed_int + 1):
    star = "*" * a
    print(star.rjust(typed_int, " "))
