# 제일 작은 수 제거하기

def solution(arr):
    answer = sorted(arr, reverse=True)[-1] # 내림차순 정렬 후 제일 작은 값 추출
    arr.remove(answer) # 제거
    
    # 배열 값이 없으면 -1 반환, 있으면 배열 반환
    if(len(arr) == 0):
        return [-1]
    return arr