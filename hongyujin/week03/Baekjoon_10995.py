import sys
n = int(sys.stdin.readline())
even = '* ' * (n - 1) + '*'
odd = ' *' * n

for i in range(n):
    if i % 2 == 0:
        print(even)
    else:
        print(odd)
