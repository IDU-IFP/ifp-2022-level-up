# 대소문자 바꾸기

word = input() # 단어 입력

# 대문자면 소문자로, 소문자면 대문자로 출력
for i in range(len(word)):
    if(word[i].isupper()):
        print(word[i].lower(), end="")
    else:
        print(word[i].upper(), end="")