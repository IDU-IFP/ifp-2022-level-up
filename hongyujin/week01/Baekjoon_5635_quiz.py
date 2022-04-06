import sys #import 문을 이용해 sys 모듈을 임포트
input = sys.stdin.readline  # 시간초과가 발생 가능, 반복문 여러줄 입력 받을 때 

n = int(input())
lst = []  #배열

for _ in range(n):
    name, d, m, y = input().rstrip().split()  #입력 받은 값을 rstrip, split 이용하여 name, d, m, y에 저장
    if len(m) == 1:
        m = '0' + m
    if len(d) == 1:
        d = '0' + d
    lst.append((name, y + m + d))

lst.sort(key = lambda x:int(x[1]))
print(lst[-1][0])
print(lst[0][0])