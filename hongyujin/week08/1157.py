s = input().lower()
sl = list(set(s))     # set() 함수를 이용하여 중복을 제거란 뒤 리스트로 묶기
first = []            # 가장 많이 사용된 알파벳

for i in sl:
    count = s.count(i)  # count 함수를 이용하여 입력 받은 단어의 개수를 세줌
    first.append(count)

if first.count(max(first)) >= 2:  # first 변수 리스트에서 가장 큰 값
    # count이용하여 개수 셈
    print("?")
else:
    print(sl[(first.index(max(first)))].upper())
