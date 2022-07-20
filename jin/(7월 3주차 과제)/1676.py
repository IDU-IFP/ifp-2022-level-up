NUM = int(input())

A = 0
while NUM > 0:
    A += NUM//5
    NUM//=5

print(A)