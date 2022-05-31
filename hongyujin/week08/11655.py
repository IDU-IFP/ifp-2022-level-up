S = input()
rot = ''
for i in S:
    if 'A' <= i <= 'Z':
        # 참일 때  if 조건식 else 거짓일때
        rot += chr((ord(i)+13) if i <= 'M' else ord(i)-13)
    elif 'a' <= i <= 'z':
        rot += chr((ord(i)+13) if i <= 'm' else ord(i)-13)
    else:
        rot += i
print(rot)
