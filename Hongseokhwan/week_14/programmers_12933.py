# 정수 내림차순으로 배치하기

def solution(n):
    res = ""
    arr = sorted(str(n), reverse=True) # 각 자리 수를 내림차순으로 정렬
    
    # 배열 요소 합치기
    for w in arr:
        res += w

    return int(res) # 정수형 변환 후 리턴