# 별찍기 - 3 

# 출력할 줄 개수 입력
N = int(input())

# 반복할떄마다 i 값을 1씩 올려 별의 개수를 1개씩 줄여가며 출력
for i in range(N):
    print('*'*(N-i))