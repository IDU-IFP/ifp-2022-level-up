# 문자열

# 문자열 개수를 입력 받인 후 문자열의 첫 문자와 마지막 문자를 출력
for _ in range(int(input())):
    word = input()
    print(word[0]+word[-1])