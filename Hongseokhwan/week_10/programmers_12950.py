# 행렬의 덧셈

def solution(arr1, arr2):
    answer = [] # 결과
    for i in range(len(arr1)):
        res = [] # 결과에 담을 배열
        for j in range(len(arr1[i])):
            res.append(arr1[i][j] + arr2[i][j]) # 배열의 요소를 합해 더한 후 배열에 저장
        answer.append(res) # 배열을 결과값에 저장
    return answer