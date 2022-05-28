t = int(input())
for i in range(t):
    n, m = map(int, input().split(' '))
    count = 0
    for i in range(n, m+1):
        str_num = str(i)
        count += str_num.count('0')
    print(count)
