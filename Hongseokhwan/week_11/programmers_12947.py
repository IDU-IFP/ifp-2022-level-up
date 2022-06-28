# 하샤드 수

def solution(x):
    arr = [] # 숫자를 담을 배열

    # 각 자리수의 숫자들을 배열에 저장
    for i in range(len(str(x))):
        arr.append(int(str(x)[i]))
    
    # 입력한 숫자가 각 자리수의 숫자들의 합으로 나누어떨어지면 true, 아니면 false
    if(x % sum(arr) == 0):
        return True
    else:
        return False