# 10808번 알파벳 개수
word = input()
alpha = [0]*26
for i in word:
    alpha[ord(i)-97]+=1
for i in alpha:
    print(i,end= ' ')