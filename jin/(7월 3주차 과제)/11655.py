TEXT = list(input())
TEXT1 = []

for i in TEXT:
    if i.isalpha(): #알파벳인지 확인
        if i.isupper():
            TEXT1.append(chr(65+(ord(i)+13-65)%26))
        else:
            TEXT1.append(chr(97+(ord(i)+13-97)%26))
    else:
        TEXT1.append(i)
print(*TEXT1, sep="")