def solution(n):
    divisors = [i for i in range(1, int(n ** .5) + 1) if n % i == 0]
    
    total = 0
    for i in divisors:
        if i == int(n / i):
            total += i
        else:
            total += (i + int(n / i))
        
    return total