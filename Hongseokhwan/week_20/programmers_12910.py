# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []
    arr.sort()
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    
    if len(answer) == 0:
        return [-1]
    return answer