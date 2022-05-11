A, B = map(int, input().split())

arr = [0]
for i in range(46):    # 범위가 1000까지여서 46을 넣는다
    for j in range(i):
        arr.append(i)  # 빈 배열에 i를 추가

print(sum(arr[A:B+1]))
