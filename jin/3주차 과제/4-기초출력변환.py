# 10진수를 입력받아 8진수(octal)로 출력
octal = int(input())
print( oct(octal)[2:] )

# 10진수를 입력받아 16진수(hexadecimal)로 출력
hexadecimal = int(input())
print( hex(hexadecimal)[2:] )

# 10진수를 입력받아 16진수(hexadecimal)로 출력
# 16진수(대문자)로 출력
hexadecimal = int(input())
hexConv = hex(hexadecimal)[2:]
print( hexConv.upper() )

# 8진수로 입력된 정수 1개를 10진수로 바꾸어 출력
octal = '0o' + input()
print( int(octal, 8) )

# 16진수로 입력된 정수 1개를 8진수로 바꾸어 출력
hexadecimal = '0x' + input()
integer = int(hexadecimal, 16)
print( oct(integer)[2:] )

# 영문자 1개를 입력받아 아스키 코드표의 10진수 값으로 출력
askii = ord(input())
print( askii )

# 10진 정수 1개를 입력받아 아스키 문자로 출력
askii = chr(int(input()))
print( askii )