# 짝수와 홀수

# 나머지가 있으면 홀수, 없으면 짝수
def solution(num):
    if(num%2): 
        answer = "Odd" 
    else: 
        answer = "Even"
    return answer