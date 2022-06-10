# 크로아티아 알파벳

arr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="] # 크로아티아 알파벳
word = input() # 단어 입력
count = 0 # 알파벳 개수를 담을 변수

# 크로아티아 알파벳을 x 로 치환하며 카운트
for alp in arr:
    while(word.count(alp)):
        count += 1
        word = word[:word.index(alp)] + 'x'*len(alp) + word[word.index(alp)+len(alp):]

# 크로아티아 알파벳 개수 + word에 저장된 단어에서 x 를 제외한 알파벳 개수 출력
print(count + len(word) - word.count('x'))