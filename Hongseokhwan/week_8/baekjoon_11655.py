# ROT13

ment = input() # 문장 입력
 
# 알파벳을 하나 따와서 13글자씩 밀어서 출력
for i in range(len(ment)):
    x = ment[i]

    if(x >= "A" and x <= "Z"):
        if(ord(x)+13 >= 91):
            x = chr(ord(x)-13)
        else:
            x = chr(ord(x)+13)
    elif(x >= "a" and x <= "z"):
        if(ord(x)+13 >= 123):
            x = chr(ord(x)-13)
        else:
            x = chr(ord(x)+13)
    print(x, end="")