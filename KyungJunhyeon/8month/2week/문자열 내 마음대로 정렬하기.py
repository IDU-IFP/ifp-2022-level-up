def solution(strings, n):
    answer = []
    n_list = []
    for string in strings:
        a = string[n] + string
        n_list.append(a)
    
    n_list.sort()
    
    for i in n_list:
        answer.append(i[1:])
    return answer