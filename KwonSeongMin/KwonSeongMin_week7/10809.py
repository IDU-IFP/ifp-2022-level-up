alpha = [-1 for _ in range(26)]

word = input()
count = 0
for w in word:
    if alpha[ord(w)-97] == -1:  # -1 이 아닌 다른 값이 들어가 있으면 최근에 어떠한 값이 삽입되어있다는 것
        alpha[ord(w)-97] = count
    count += 1

for res in alpha:
    print(res,end=' ')