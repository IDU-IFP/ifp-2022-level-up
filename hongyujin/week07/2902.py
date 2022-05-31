a = list(input().split('-'))   # a는 리스트
for i in a:                    # range(len(a))은 에러남
    print(i[0], end='')
