a = int (input())
b = a
for i in range(0,a):
    print(' '*i+'*' * (2*(b - i)-1))