n = int(input())
for i in range(5):
    s = input()
    s = s[0].upper() + s[1:]   # n[0]와 n[1:]로 첫 글자와  다음 글자를 분리한다
    print(s)                   # upper -> 소무자을 대문자로 바꾸는 함수
