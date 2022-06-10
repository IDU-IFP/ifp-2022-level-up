t = int(input())
for i in range(t):
    n, m = map(int, input().split(' '))
    count = 0
    for i in range(n, m+1):
        str_num = str(i)      # 정수를 문자열로 변환 후 저장한다
        count += str_num.count('0')   # 0의 개수를 센 후 더해준다
    print(count)
