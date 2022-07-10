#https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    a = arr[0]  # 첫번째값을 저장
    
    for i in arr:
        if a > i:   
            a = i   # 최소값을 걸러내는 부분

    arr.pop(arr.index(a))   # 최소값의 위치에 있는 값을 제거
        
    if len(arr):
        return arr
    else:
        return [-1] # 배열이 없는 것을 확인하는 부분

print(solution([2,3,4]))    # 실험 코드