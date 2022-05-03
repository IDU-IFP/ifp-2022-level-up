#https://www.acmicpc.net/problem/2592

arr = []
m = 0   #최빈값 구하기 위한 변수
n = 0   #최빈값을 담을 변수
for _ in range(10):
    num = int(input())
    arr.append(num)
    if arr.count(num) > m:  #최빈값 구하는 분기문
        m = arr.count(num)  #몇 개가 가장 많은지 
        n = num #최빈값
print(sum(arr)//10)
print(n)
    