#https://www.acmicpc.net/problem/2902

res = []

word = input()
for i in word:
    if i < 'a' and i != '-':    #대문자이지만 -의 값이 아닐 경우
        res.append(i)

for i in res:
    print(i,end='')