def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        templist1 = arr1[i]
        templist2 = arr2[i]
        for i in range(len(templist1)):
            temp.append(templist1[i] + templist2[i])
        answer.append(list(temp))
    return answer
