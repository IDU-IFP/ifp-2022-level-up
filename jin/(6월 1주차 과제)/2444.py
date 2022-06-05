a = int(input())
b = a
for i in range(1, a + 1):
    print(' '*(b-i)+'*'*(2*i-1))
for k in range(1,a):
    print(' '*k+'*'*(2*(b-k)-1))