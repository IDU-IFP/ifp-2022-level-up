# 모음의 개수

words = ['a', 'e', 'i', 'o', 'u'] # 모음을 세기 위한 배열
sum = 0 # 모음 개수를 세기 위한 변수

input_word = input() # 단어 입력

# 모음 카운트
for word in words:
    sum += input_word.count(word)

# 출력
print(sum)