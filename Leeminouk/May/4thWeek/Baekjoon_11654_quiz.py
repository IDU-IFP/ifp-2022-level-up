# 문제
# 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

# 입력
# 알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.

# 출력
# 입력으로 주어진 글자의 아스키 코드 값을 출력한다.

import string

ascii_code = {"A": 65, "a": 97, "0": 48}
lower = {b: a for a, b in enumerate(string.ascii_lowercase)}
upper = {b: a for a, b in enumerate(string.ascii_uppercase)}

typed = input()

if typed in lower:
    print(ascii_code["a"] + lower[typed])

elif typed in upper:
    print(ascii_code["A"] + upper[typed])

else:
    print(ascii_code["0"] + int(typed))