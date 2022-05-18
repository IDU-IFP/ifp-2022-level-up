# 알파벳 찾기

alpha_arr = [-1 for i in range(26)] # 알파벳 개수만큼 -1을 저장한 배열
word = input() # 단어 입력

# 단어 각각의 알파벳이 처음 등장하는 위치를 배열에 저장
for i in range(len(word)):
    if(alpha_arr[ord(word[i]) - 97] == -1):
        alpha_arr[ord(word[i]) - 97] = i

# 배열을 공백으로 구분해 출력
print(*alpha_arr, sep=" ")