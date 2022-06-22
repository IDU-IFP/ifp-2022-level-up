def solution(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum / len(arr)  # 더한 값들을 arr 리스트 값들의 통 개수로 나누어 줌
