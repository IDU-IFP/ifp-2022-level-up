#https://programmers.co.kr/learn/courses/30/lessons/12950
def solution(arr1, arr2):
    a = []
    answer = []
    for x, y in zip(arr1, arr2):
        for i in range(len(arr1[0])):
            a.append(x[i]+y[i])
        answer.append(a)
        a = []
    return answer
