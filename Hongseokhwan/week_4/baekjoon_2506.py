# 점수계산

n = int(input()) # 문제의 개수 입력
answer = input().split(" ") # 문제의 채점 결과 입력
k = 0 # 각 문제에 대한 점수를 담을 변수 선언
sum = 0 # 점수의 총합을 담을 변수 선언

# 가산점을 고려한 총 점수 계산
for i in range(n):
    if(answer[i] == '1' and answer[i-1] == '1'):
        k += 1 
        sum += k
    elif(answer[i] == '1'):
        k = 1
        sum += k

# 출력
print(sum)