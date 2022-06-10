# 11655번 ROT13
n = input()
caesar = ''
for i in range(len(n)):
    if n[i] == ' ' or ord(n[i]) < ord('A'):
        caesar += n[i]
    else:
        if ord(n[i]) + 13 > 122:
            caesar += chr(96 + (ord(n[i]) + 13) - 122)
        elif ord(n[i]) + 13 > 90 and ord(n[i]) < 91:
            caesar += chr(64 + (ord(n[i]) + 13) - 90)
        else:
            caesar += chr(ord(n[i]) + 13)
print(caesar)