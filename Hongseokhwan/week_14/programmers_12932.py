# 자연수 뒤집어 배열로 만들기

def solution(n):
    arr = list(str(n)[::-1]) # 문자열로 변환 후 뒤집기
    
    for i in range(len(arr)):
        arr[i] = int(arr[i]) # 정수형 변환
        
    return arr