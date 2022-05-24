word = input()
for res in word:
    if res <= 'Z':  #대문자이면?
        print(chr(ord(res)+32),end='')  #소문자 변환 (32는 유니코드 a-A의 값)
    else:   #아니면?
        print(chr(ord(res)-32),end='')  #대문자 변환