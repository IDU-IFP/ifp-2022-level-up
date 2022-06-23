num = int(input())

for i in range(1, num+1):
    count = 'X' if '3' in str(i) or '6' in str(i) or '9' in str(i) else i
    print(count, end=' ')
