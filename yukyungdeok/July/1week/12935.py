# 12935번 제일 작은 수 제거하기(프로그래머스)
def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        
        return arr
    else:
        return [-1]