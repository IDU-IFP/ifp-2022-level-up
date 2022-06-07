# 단어 공부

word = input().upper() # 입력 문자를 대문자로 변환
alpha_dic = {} # 알파벳을 셀 딕셔너리

# 알파벳의 아스키코드로 만들어진 키가 없으면 만들어서 카운트 1
# 있다면 키에 해당하는 값을 +1
for alpha in word:
    key = ord(alpha)
    if(not key in alpha_dic):
        alpha_dic[key] = 1
    else:
        alpha_dic[key] += 1

# 딕셔너리 값의 최대값을 배열에 저장
res = [k for k,v in alpha_dic.items() if max(alpha_dic.values()) == v]

# 배열의 값이 하나면 값 출력, 아니면 ? 출력
if(len(res) == 1):
    print(chr(*res))
else:
    print("?")