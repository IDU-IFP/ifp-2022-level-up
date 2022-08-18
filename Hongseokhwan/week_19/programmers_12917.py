# 문자열 내림차순으로 배치하기

def solution(s):
    arr = []
    for word in s:
        arr.append(word)
    arr.sort(reverse=True)
    return  ''.join(arr)