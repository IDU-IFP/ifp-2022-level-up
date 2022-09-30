def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        t = bin(a | b)
        room = str(t)
        s = len(room[2:])
        if s < n:
            val = ([0] * (n - s)) + room[2:]
            
    return val