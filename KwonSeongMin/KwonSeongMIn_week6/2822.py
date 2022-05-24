#https://www.acmicpc.net/problem/2822

x = [0 for _ in range(8)]   #입력값을 받을 수, append 함수 대신 입력받은 값 저장하려고 0을 8번 대입
res = []
for i in range(8):
    n = int(input())
    x[i] = n    #입력받는 수 대입
    
sortx = sorted(x, reverse=True) #sortx list문을 만들어 x list를 내림차순으로 정렬

print(sum(sortx[0:5]))  #1~5번째 수를 더해줌.
for i in range(5):    #sortx에 있는 수의 위치값을 res list에 append
    res.append(x.index(sortx[i])+1)
    
res.sort()  #결과값 오름차순 정렬
for i in res:
    print(i,end=' ')