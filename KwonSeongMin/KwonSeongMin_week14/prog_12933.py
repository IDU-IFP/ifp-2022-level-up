#https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    result = ''.join(sorted(str(n), reverse=True))
    # 1. 먼저 n을 str형으로 변환 후 내림차순 정렬
    # 2. ["3","2","1"] 이런 식으로 변수가 저장되는데 join함수로 깔끔하게 저장
    return int(result)
