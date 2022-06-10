#https://www.acmicpc.net/problem/1978

t = int(input())
n = list(map(int,input().split()))
for i in n:
    count = 0
    k = 1
    
    while i >= k:   # 1부터 자기 자신의 수 까지 나눠서 나머지가 0이면 count 한다.
        if i % k == 0:  # 이유는 소수 뜻이 1과 자기 자신만으로 나눠지는 수이기 때문
            count += 1
        k += 1      
        
    if count == 2:  #그러므로 count가 2, 즉 1과 자기 자신으로만 나눠졌으면 결과값 count
        t -= 1
       
print(t)