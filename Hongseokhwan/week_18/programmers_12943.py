# 콜라츠 추측

def solution(num):
    count = 0 # 카운트
    if(num==1): # 주어진 수가 1이면 0 반환
        return 0
    while(num != 1): # 1이 될때까지 반복
        if(num%2==0): # 짝수면 2로 나누기
            num = num // 2 
        else: # 홀수면 3을 곱하고 1을 더하기
            num = num*3+1
        count += 1
        if(count==500): # 500번 반복이 되면 -1 반환
            return -1
    return count # 횟수 반환