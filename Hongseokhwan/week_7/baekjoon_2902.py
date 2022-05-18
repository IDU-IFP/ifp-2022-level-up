# KMP는 왜 KMP일까?

# '-' 을 기준으로 단어를 반복. 단어의 첫 글자만 가져와 이어서 출력
for word in input().split("-"):
    print(word[0], end="")