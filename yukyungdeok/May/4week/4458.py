# 4458번 첫 글자를 대문자로
for _ in range(int(input())):
    n = str(input())
    n= n[0].upper()+n[1:]
    print(n)