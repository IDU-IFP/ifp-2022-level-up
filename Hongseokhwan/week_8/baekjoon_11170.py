# 0의 개수

# 테스트 케이스만큼 반복
# n부터 m까지의 수 중 0의 개수를 카운트 후 출력
for _ in range(int(input())):
    count = 0
    n,m=map(int,input().split())
    
    for i in range(n,m+1):
        alpha = str(i)
        count += alpha.count("0")
    
    print(count)