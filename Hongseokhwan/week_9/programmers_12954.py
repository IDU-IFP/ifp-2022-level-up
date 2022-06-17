# x만큼 간격이 있는 n개의 숫자

x,n = map(int, input().split()) # 간격과 개수를 입력

# 입력한 간격과 개수만큼 수를 배열에 저장
def solution(x, n):
    answer = [x*i for i in range(1,n+1)]
    return answer

# 출력
print(solution(x, n))