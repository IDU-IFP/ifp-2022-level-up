# 첫 글자를 대문자로

# 문장 개수를 입력받아 첫글자를 대문자로 변환 후 출력
for _ in range(int(input())):
    ment = input()
    print(ment[0].upper()+ment[1:])