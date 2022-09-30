def solution(n):
    counter = 0
    word_list = []
    for _ in range(n):
        if counter == 0:
            word_list.append("수")
            counter = 1
        else:
            word_list.append("박")
            counter = 0
    answer = "".join(word_list)
    return answer