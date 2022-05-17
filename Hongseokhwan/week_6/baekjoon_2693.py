# N번째 큰 수
 
# 테스트 케이스 만큼 반복. 입력한 10개의 값 중 3번째로 큰 값을 출력
for _ in range(int(input())):
    print(sorted(list(map(int, input().split())), reverse=True)[2])