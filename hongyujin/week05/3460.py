T = int(input())

for _ in range(T):
    n = bin(int(input()))[2:]  # bin함수를 이요하면 2진수로 변환됨, [2:]는 2번째 문자열부터 보여줌
    for i in range(len(n)):
        if n[-i - 1] == '1':     # 2진수의 값을 역순으로 보기 위해
            print(i, end=' ')  # end를 이용해 문자 출력 후 공백을 출력
