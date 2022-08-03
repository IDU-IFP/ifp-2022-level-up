# 소수 찾기

def solution(n): # 에라토스테네스의 체 사용
    bool_arr = [True for i in range(n+1)]
    m = int(n**0.5)
    
    for i in range(2,m+1):
        if(bool_arr[i] == True):
            for j in range(i*2,n+1,i):
                bool_arr[j] = False
    
    return bool_arr[2:].count(True)