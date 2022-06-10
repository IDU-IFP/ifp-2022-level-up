#https://www.acmicpc.net/problem/11655

l = input()
for i in l:
    if i.isupper(): # 대문자일 떄
        s = ord(i) - 13
        if s < 65:  # 대문자 범위를 넘어서면 더해줌
            s += 26
    elif i.islower():   # 소문자일 때
        s = ord(i) - 13
        if s < 97:  # 소문자 범위를 넘어서면 더해줌
            s += 26
    else:
        print(i,end='') # 공백, 숫자일 때
        continue
            
    print(chr(s),end='')