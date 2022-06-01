# 링크
# https://www.acmicpc.net/problem/2941

# 크로아티아 알파벳

# 문제
# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

# 크로아티아 알파벳	변경
# č	c=
# ć	c-
# dž	dz=
# đ	d-
# lj	lj
# nj	nj
# š	s=
# ž	z=
# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

# 입력
# 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.

# 단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

# 출력
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

# 예제 입력 1
# ljes=njak
# 예제 출력 1
# 6
# 예제 입력 2
# ddz=z=
# 예제 출력 2
# 3
# 예제 입력 3
# nljj
# 예제 출력 3
# 3
# 예제 입력 4
# c=c=
# 예제 출력 4
# 2
# 예제 입력 5
# dz=ak
# 예제 출력 5
# 3

# 함수 -----------------------------------------------------------
def solution_case1():  # 68ms
    word = input()
    l = len(word)
    cnt = 0
    for i in range(l-1):
        if word[i] == "c":
            if word[i+1] == "=" or word[i+1] == "-":
                cnt += 1
        if word[i] == "d":
            if word[i+1] == "-" or word[i+1:i+3] == "z=":
                cnt += 1
        if word[i:i+2] == "lj" or word[i:i+2] == "nj" or word[i:i+2] == "s=" or word[i:i+2] == "z=":
            cnt += 1
    print(l-cnt)


def len2Word(str):
    return str in {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="}


def len3Word(str):
    return str in {"dz="}


def solution_case2():  # 72ms
    word = input()
    l = len(word)
    cnt = 0

    for i in range(l-1):
        if len2Word(word[i:i+2]):
            cnt += 1
        if len3Word(word[i:i+3]):
            cnt += 1

    print(l-cnt)


# 실행 ------------------------------------------------------------
solution_case2()
