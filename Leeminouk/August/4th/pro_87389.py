def solution(n):
    half = int(n ** 0.5)
    answer = 0
    
    for i in range(1, half):
        if n % i == 1:
            answer = i
            break
    
    if answer == 0:
        for i in range(half, n):
            if n % i == 1:
                answer = i
                break
    
    return answer